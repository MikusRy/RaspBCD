import RPi.GPIO as GPIO


def setup(pins: list):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        for index in pins:
            GPIO.setup(index, GPIO.OUT)
    except Exception as ex:
        print(ex)