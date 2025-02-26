"""
Humidity sensor tool for the agent.
"""
import sys
from typing import Any, Dict

sys.path.append("rasp_pi_workshop")  # To import from the repository
from rasp_pi_workshop import read_sensor_humidity, INVALID_VALUE

from rasp_pi_workshop.tools.base import DocumentedTool


class HumidityTool(DocumentedTool):
    """
    Tool for getting the current humidity from the DHT22 sensor.
    """
    
    name = "humidity_sensor"
    description = "Gets the current humidity from the DHT22 sensor"
    
    def _execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get the current humidity from the sensor.
        
        Returns:
            Dict[str, Any]: A dictionary containing the humidity data
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
