
from flask import Flask, render_template, jsonify

import RPi.GPIO as GPIO
from PyCode import QQCar
import atexit

atexit.register(GPIO.cleanup)


app = Flask(__name__)


# 首页
@app.route("/")
def index():
    return render_template('index.html')


# 驾驶
@app.route('/drive/<action>', methods=['GET'])
def drive(action):
    if action == 'forward':
        car.forward()
    if action == 'backOff':
        car.backOff()
    if action == 'leftTurn':
        car.leftTurn()
    if action == 'rightTurn':
        car.rightTurn()
    if action == 'stop':
        car.stop()
    return jsonify({'success': 'ok'})


# 超声波云台
@app.route('/servoUltrasonic/<action>', methods=['GET'])
def servoUltrasonic(action):
    if action == 'leftTurn':
        car.servoUltrasonicTurnLeft()
    if action == 'rightTurn':
        car.servoUltrasonicTurnRight()
    return jsonify({'success': 'ok'})


# 摄像头云台
@app.route('/servoCamera/<action>', methods=['GET'])
def servoCamera(action):
    if action == 'leftTurn':
        car.servoCameraHTurnLeft()
    if action == 'rightTurn':
        car.servoCameraHTurnRight()
    if action == 'upTurn':
        car.servoCameraVTurnUp()
    if action == 'downTurn':
        car.servoCameraVTurnDown()
    return jsonify({'success': 'ok'})


# 大灯
@app.route('/light/<action>', methods=['GET'])
def light(action):
    if action == 'turnOn':
        car.turnOnLight()
    if action == 'turnOff':
        car.turnOffLight()
    return jsonify({'success': 'ok'})


# 避障
@app.route('/autocross/<action>', methods=['GET'])
def autocross(action):
    if action == 'turnOn':
        car.turnOnAutoCross()
    if action == 'turnOff':
        car.turnOffAutoCross()
    return jsonify({'success': 'ok'})


# 寻迹
@app.route('/cruise/<action>', methods=['GET'])
def cruise(action):
    if action == 'turnOn':
        car.turnOnCruise()
    if action == 'turnOff':
        car.turnOffCruise()
    return jsonify({'success': 'ok'})


# 重置
@app.route('/reset', methods=['GET'])
def reset():
    GPIO.cleanup()
    return jsonify({'success': 'ok'})


car = QQCar.QQCar()

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except Exception as e:
        GPIO.cleanup()
