import random
import RPi.GPIO as GPIO
from numpy import binary_repr


def turnON(led: list, result):
    try:
        for i in range(0, len(led)):
            if result[i] == "1":
                GPIO.output(led[i], GPIO.HIGH)
        return True
    except Exception as ex:
        print(ex)
        turnOFF(led)


def turnOFF(led: list):
    try:
        for item in led:
            GPIO.output(item, GPIO.LOW)
        return True
    except Exception as ex:
        print(ex)
        return False


def randomLED():
    """
    Randoms from range 0 to 99.
    Saves value in BCD representation.
    :return: table -> [ value: str, binary_dozens: str, binary_units: str ]
    """
    try:
        temp = str(random.randint(0, 99))
        if len(temp) == 2:
            temp = [temp, int(temp[0]), int(temp[1])]
            return [temp[0], binary_repr(temp[1], width=4), binary_repr(temp[2], width=4)]
        else:
            temp = [temp, 0, int(temp[1])]
            return [temp[0], binary_repr(temp[1], width=4), binary_repr(temp[2], width=4)]
    except Exception as ex:
        print(ex)
        return None


