"""
Humidity sensor tool for the agent.
"""
from typing import Any, Dict

from rasp_pi_workshop import read_sensor_humidity, INVALID_VALUE


def measure_humidity() -> Dict[str, Any]:
    """
    Tool for getting the current humidity from the DHT22 sensor.

    Doesn't require any argument as an input.

    Args:
        None

    Returns:
        Dict[str, Any]: A dictionary containing the humidity data. If the humidity data is invalid, an error message is returned.
        Has the status key with the value "success" if the humidity data is valid, and "error" if the humidity data is invalid.
        If the humidity data is valid, the dictionary contains the "humidity" value and the "unit" of measurement.
    """
    humidity = read_sensor_humidity()

    if humidity == INVALID_VALUE:
        return {
            "error": "Failed to read humidity from sensor",
            "status": "error"
        }

    return {
        "humidity": humidity,
        "unit": "percent",
        "status": "success"
    }
