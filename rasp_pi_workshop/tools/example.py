"""
Example tool template for creating custom tools.
"""
from typing import Any, Dict


def example_tool_function(input: str) -> Dict[str, Any]:
    """ An example function that takes a string input and returns a dictionary with the input and a greeting. """
    return {"input": input, "output": f"Hello, {input}!"}


"""
How to register your tool with the agent:

from llama_index.core.tools import FunctionTool

example_tool = FunctionTool().from_function(fn=example_tool_function)

# In your main.py or agent setup:
agent = create_agent(
    llm=llm,
    tools=[
        example_tool, # Your custom tool
    ]
)
"""
