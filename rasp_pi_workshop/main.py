from time import sleep
from rasp_pi_workshop import *
from rasp_pi_workshop.__motor_controll__ import *

'''
List of available commands:

    print("This is my message")

    led_on()
    count()
    sleep(5)
    led_off()

    read_sensor_temperature()
    read_sensor_humidity()
'''


def main():
    # Connect to the Raspberry Pi
    connect()

    # Your code goes here

    # Your code ends here

    # Disconnect from the Raspberry Pi
    exit_sensor()

    return 0


if __name__ == "__main__":
    main()
