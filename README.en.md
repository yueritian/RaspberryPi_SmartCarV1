# RaspberryPi Smart Car V1

[English](README.en.md) | [中文](README.md)

A Raspberry Pi smart car controlled from a mobile-friendly web interface, with a live camera stream and multiple sensors.

![Smart car model](DocImages/model.jpg)

## Features

- Web-based driving controls
- Live MJPEG camera stream
- Camera and ultrasonic-sensor gimbals
- Infrared and ultrasonic obstacle warnings
- Line-tracking sensor alerts
- Automatic lighting based on ambient light
- LCD status display and buzzer alerts

## Hardware

The original build used a Raspberry Pi 3, an L298N motor driver, two TT motors, three SG90 servos, a Raspberry Pi camera, an LCD1602 with an I2C adapter, infrared obstacle sensors, a line-tracking sensor, an ultrasonic sensor, a light sensor, a passive buzzer, and an RGB light.

GPIO uses physical board numbering (`GPIO.BOARD`). Review the pin assignments in `PyCode/QQCar.py` before connecting hardware.

## Quick start

> This project was originally built in 2018 for Raspbian Stretch. On a current Raspberry Pi OS image, mjpg-streamer paths and startup options may differ.

```bash
git clone https://github.com/yueritian/RaspberryPi_SmartCarV1.git
cd RaspberryPi_SmartCarV1
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 Web.py
```

Open `http://<raspberry-pi-ip>:5000`. By default, the web interface reads the camera stream from `http://<raspberry-pi-ip>:8080/?action=stream`.

Configuration is available through environment variables:

```bash
export HOST=0.0.0.0
export PORT=5000
export CAMERA_STREAM_URL='http://192.168.1.10:8080/?action=stream'
python3 Web.py
```

The interface selects Chinese or English from the browser preference. Use the switch in the upper-left corner, or open `/?lang=zh` and `/?lang=en` directly.

## Camera streamer

The legacy `start.sh` expects mjpg-streamer at `/usr/local/bin/mjpg_streamer`, with plugins in `/usr/local/lib`. Adjust these paths to match your installation. You can also start the Flask service and camera streamer separately.

## Safety and security

The control API currently has no authentication. Run it only on a trusted local network and do not expose it directly to the internet. Verify all wiring and power rails before starting the software; motors, the Raspberry Pi, and peripherals may require different supply voltages.

## Original environment

- Raspberry Pi 3
- Raspbian Stretch Lite (2018-04-18)
- Python 3.6.4
- Flask
- mjpg-streamer

## License

Apache License 2.0. See [LICENSE](LICENSE).
