"""
Interactive main file for the Raspberry Pi Smart Home Agent.

This file provides an interactive interface for the agent, showing
the agent's thinking process and tool usage. It's designed to be
educational for beginners to understand how the agent works and
how to create custom tools.

Usage:
    python main_inter.py
"""
import sys

# Add the repository to the path
sys.path.append("rasp_pi_workshop")
from rasp_pi_workshop import connect, exit_sensor

# Import agent components
from agent.llm import setup_llm
from agent.agent import create_agent
from agent.interactive import interactive_agent_loop

# Import tools
from tools.temperature import TemperatureTool
from tools.humidity import HumidityTool


def main():
    """
    Main function to run the interactive agent.
    """
    print("Initializing Raspberry Pi Smart Home Agent...")
    
    # Connect to the Raspberry Pi
    connect()
    
    # Setup LLM with vLLM
    print("Setting up LLM...")
    llm = setup_llm(
        model="smollm2:360m",  # Replace with your model name
        temperature=0.4,
        max_tokens=4096,
        api_base="http://localhost:11434",
        timeout=360
    )
    
    # Create agent with tools
    print("Creating agent with tools...")
    agent = create_agent(
        llm=llm,
        tools=[
            TemperatureTool(),
            HumidityTool(),
            # Add more tools here as needed
        ]
    )
    
    # Start interactive loop
    interactive_agent_loop(agent)

    print("Exiting Raspberry Pi Smart Home Agent...")

    # Disconnect from the Raspberry Pi
    exit_sensor()

    return 0


if __name__ == "__main__":
    main()
