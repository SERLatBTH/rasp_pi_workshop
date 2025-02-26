"""
Temperature sensor tool for the agent.
"""
from typing import Any, Dict

from rasp_pi_workshop import read_sensor_temperature, INVALID_VALUE


def measure_temperature() -> Dict[str, Any]:
    """
    Get the current temperature from the DHT22 sensor.
    Returns the JSON structure with `temperature`, `unit` as of unit of temperature and function call `status`
    (can be either 'success' or 'error').

    Doesn't require any argument as an input.

    Args:
        None

    Returns:
        Dict[str, Any]: A dictionary containing the temperature data
        Has the "status" key with the value "success" if the temperature data is valid, and "error" if the temperature data is invalid.
        If the temperature data is valid, the dictionary contains the "temperature" value and the "unit" of measurement.
    """
    temperature = read_sensor_temperature()

    if temperature == INVALID_VALUE:
        return {
            "error": "Failed to read temperature from sensor",
            "status": "error"
        }

    return {
        "temperature": temperature,
        "unit": "Celsius",
        "status": "success"
    }
