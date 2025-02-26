"""
Python code execution tool for the agent.
"""
from typing import Any, Dict

from rasp_pi_workshop import connect, count, led_off, led_on, \
        read_sensor_humidity, read_sensor_temperature, \
        exit_sensor


def py_code_exec(code_as_str: str) -> None:
    """
    Tool to get the python code and execute it.
    Note: Consider to call following functions during code creation:
    - read_sensor_temperature() # to get the current temperature
    - read_sensor_humidity() # to get the current humidity
    - led_on() # to turn on the LED
    - led_off() # to turn off the LED
    - count() # atomic counter that increments by 1
    - print() # to print the message


    Args:
        code_as_str (str): Python code as string to execute

    Returns:
        None
    """
    print("Executing the Python code...")
    print("=====================================")
    print(code_as_str)
    print("=====================================")

    # Execute the code
    exec(code_as_str)
