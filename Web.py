
import atexit
import os

from flask import Flask, jsonify, render_template, request
import RPi.GPIO as GPIO

from PyCode import QQCar

atexit.register(GPIO.cleanup)


app = Flask(__name__)

TRANSLATIONS = {
    'zh': {
        'app_title': '树莓派智能小车',
        'obstacle_avoidance': '避障',
        'line_tracking': '寻迹',
        'lighting': '照明',
        'turn_on': '开启',
        'turn_off': '关闭',
        'camera_gimbal': '摄像头云台',
        'ultrasonic_gimbal': '超声波云台',
        'move_forward': '前进',
        'move_backward': '后退',
        'turn_left': '左转',
        'turn_right': '右转',
        'camera_up': '摄像头向上',
        'camera_down': '摄像头向下',
        'camera_left': '摄像头向左',
        'camera_right': '摄像头向右',
        'ultrasonic_left': '超声波云台向左',
        'ultrasonic_right': '超声波云台向右',
        'switch_language': 'English',
        'request_failed': '控制请求失败',
    },
    'en': {
        'app_title': 'Raspberry Pi Smart Car',
        'obstacle_avoidance': 'Avoid',
        'line_tracking': 'Track',
        'lighting': 'Light',
        'turn_on': 'On',
        'turn_off': 'Off',
        'camera_gimbal': 'Camera gimbal',
        'ultrasonic_gimbal': 'Ultrasonic gimbal',
        'move_forward': 'Move forward',
        'move_backward': 'Move backward',
        'turn_left': 'Turn left',
        'turn_right': 'Turn right',
        'camera_up': 'Tilt camera up',
        'camera_down': 'Tilt camera down',
        'camera_left': 'Pan camera left',
        'camera_right': 'Pan camera right',
        'ultrasonic_left': 'Turn ultrasonic sensor left',
        'ultrasonic_right': 'Turn ultrasonic sensor right',
        'switch_language': '中文',
        'request_failed': 'Control request failed',
    },
}


def get_language():
    requested = request.args.get('lang', '').lower()
    if requested in TRANSLATIONS:
        return requested

    saved = request.cookies.get('language', '').lower()
    if saved in TRANSLATIONS:
        return saved

    return request.accept_languages.best_match(TRANSLATIONS.keys()) or 'en'


def get_camera_stream_url():
    configured_url = os.environ.get('CAMERA_STREAM_URL')
    if configured_url:
        return configured_url

    hostname = request.host.split(':', 1)[0]
    return 'http://{}:8080/?action=stream'.format(hostname)


def run_action(action, actions):
    handler = actions.get(action)
    if handler is None:
        return jsonify({'success': False, 'error': 'invalid_action'}), 404
    handler()
    return jsonify({'success': True, 'action': action})


# 首页
@app.route("/")
def index():
    language = get_language()
    response = app.make_response(render_template(
        'index.html',
        camera_stream_url=get_camera_stream_url(),
        language=language,
        next_language='en' if language == 'zh' else 'zh',
        translations=TRANSLATIONS[language],
    ))
    if request.args.get('lang', '').lower() in TRANSLATIONS:
        response.set_cookie('language', language, max_age=31536000, samesite='Lax')
    return response


# 驾驶
@app.route('/drive/<action>', methods=['GET'])
def drive(action):
    return run_action(action, {
        'forward': car.forward,
        'backOff': car.backOff,
        'leftTurn': car.leftTurn,
        'rightTurn': car.rightTurn,
        'stop': car.stop,
    })


# 超声波云台
@app.route('/servoUltrasonic/<action>', methods=['GET'])
def servoUltrasonic(action):
    return run_action(action, {
        'leftTurn': car.servoUltrasonicTurnLeft,
        'rightTurn': car.servoUltrasonicTurnRight,
    })


# 摄像头云台
@app.route('/servoCamera/<action>', methods=['GET'])
def servoCamera(action):
    return run_action(action, {
        'leftTurn': car.servoCameraHTurnLeft,
        'rightTurn': car.servoCameraHTurnRight,
        'upTurn': car.servoCameraVTurnUp,
        'downTurn': car.servoCameraVTurnDown,
    })


# 大灯
@app.route('/light/<action>', methods=['GET'])
def light(action):
    return run_action(action, {
        'turnOn': car.turnOnLight,
        'turnOff': car.turnOffLight,
    })


# 避障
@app.route('/autocross/<action>', methods=['GET'])
def autocross(action):
    return run_action(action, {
        'turnOn': car.turnOnAutoCross,
        'turnOff': car.turnOffAutoCross,
    })


# 寻迹
@app.route('/cruise/<action>', methods=['GET'])
def cruise(action):
    return run_action(action, {
        'turnOn': car.turnOnCruise,
        'turnOff': car.turnOffCruise,
    })


# 重置
@app.route('/reset', methods=['GET'])
def reset():
    GPIO.cleanup()
    return jsonify({'success': 'ok'})


car = QQCar.QQCar()

if __name__ == '__main__':
    try:
        app.run(
            host=os.environ.get('HOST', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
        )
    except Exception:
        app.logger.exception('Smart car web service stopped unexpectedly')
        GPIO.cleanup()
        raise
