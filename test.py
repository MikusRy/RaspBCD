import time
from RaspSETUP import setup
from led_manager import turnON, turnOFF, randomLED


if __name__ == "__main__":
    # RASPBERRY SETUP
    first = [21, 20, 16, 12]
    second = [26, 19, 13, 6]
    setup(first + second)

    # RANDOM VALUE FROM 0 TO 99, AND CONVERT IT TO BINARY REPRESENTATION
    value = randomLED()

    while(True):
        print("Wylosowana wartość to " + value[0])

        print("LED ON")
        turnON(first, value[1])
        turnON(second, value[2])
        time.sleep(1)

        print("LED OFF")
        turnOFF(first)
        turnOFF(second)
        time.sleep(1)
