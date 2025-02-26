"""
Example tool template for creating custom tools.
"""
from typing import Any, Dict

from rasp_pi_workshop.tools.base import DocumentedTool


class ExampleTool(DocumentedTool):
    """
    Example template for creating a custom tool.
    
    Steps to create your own tool:
    1. Choose a descriptive name and description
    2. Define any parameters your tool needs
    3. Implement the _execute method with your tool's logic
    4. Return results in a structured format
    """
    
    # Tool name (used by the agent to identify this tool)
    name = "example_tool"
    
    # Description (helps the agent understand when to use this tool)
    description = "This is an example tool that demonstrates how to create custom tools"
    
    def _execute(self, parameter1: str = "", parameter2: int = 0, **kwargs: Any) -> Dict[str, Any]:
        """
        This is where your tool's logic goes.
        
        Args:
            parameter1: A string parameter example
            parameter2: An integer parameter example
            **kwargs: Additional keyword arguments
            
        Returns:
            A dictionary with the results of your tool
        """
        # Your tool's logic here
        result = f"Processed: {parameter1} with value {parameter2}"
        
        # Always return a dictionary with your results
        return {
            "result": result,
            "status": "success"
        }


"""
How to register your tool with the agent:

from tools.example import ExampleTool

# In your main.py or agent setup:
agent = create_agent(
    llm=llm,
    tools=[
        TemperatureTool(),
        HumidityTool(),
        ExampleTool(),  # Your custom tool
    ]
)
"""
