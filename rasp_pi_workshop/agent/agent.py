"""
ReAct agent implementation module.
"""
from typing import List, Optional

from llama_index.core.agent import ReActAgent
from llama_index.core.llms.llm import LLM
from llama_index.core.tools import BaseTool


def create_agent(llm: LLM, tools: Optional[List[BaseTool]] = None, max_iterations: int = 10) -> ReActAgent:
    """
    Create a ReAct agent with the provided LLM and tools.
    
    Args:
        llm (LLM): The language model to use
        tools (List[BaseTool], optional): List of tools to register with the agent
        
    Returns:
        ReActAgent: The configured agent
    """
    # Create agent
    agent = ReActAgent.from_tools(
        tools=tools,
        llm=llm,
        verbose=True,
        max_iterations=max_iterations
    )
    
    return agent
