"""
Temperature sensor tool for the agent.
"""
import sys
from typing import Any, Dict

sys.path.append("rasp_pi_workshop")  # To import from the repository
from rasp_pi_workshop import read_sensor_temperature, INVALID_VALUE

from rasp_pi_workshop.tools.base import DocumentedTool


class TemperatureTool(DocumentedTool):
    """
    Tool for getting the current temperature from the DHT22 sensor.
    """
    
    name = "temperature_sensor"
    description = "Gets the current temperature from the DHT22 sensor.\n" \
                  "Returns the JSON structure with `temperature`, `unit` as of unit of temperature and "\
                  "function call `status` (can be either 'success' or 'error')."

    
    def _execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get the current temperature from the sensor.
        
        Returns:
            Dict[str, Any]: A dictionary containing the temperature data
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
