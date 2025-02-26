"""
Interactive agent loop module.
"""
from typing import Any, Dict

from llama_index.core.agent import ReActAgent
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler


class VerboseCallback(LlamaDebugHandler):
    """
    Callback handler that prints verbose output for the agent's thinking process.
    """
    
    def __init__(self):
        super().__init__(print_trace_on_end=False)
        self.thinking_steps = []
    
    def on_agent_start(self, query: str, **kwargs: Any) -> None:
        """Called when agent starts processing a query."""
        print(f"\n📝 QUERY: {query}")
    
    def on_agent_finish(self, **kwargs: Any) -> None:
        """Called when agent finishes processing a query."""
        pass
    
    def on_new_token(self, token: str, **kwargs: Any) -> None:
        """Called when a new token is generated."""
        pass
    
    def on_agent_step(self, step: Dict[str, Any], **kwargs: Any) -> None:
        """Called on each agent step."""
        if "reasoning" in step:
            print(f"\n🤔 REASONING:\n{step['reasoning']}")
        
        if "action" in step:
            action = step["action"]
            print(f"\n🔧 SELECTED TOOL: {action.tool}")
            print(f"📋 TOOL INPUT: {action.tool_input}")
        
        if "observation" in step:
            print(f"\n📤 TOOL RESULT: {step['observation']}")
    
    def on_agent_error(self, error: Exception, **kwargs: Any) -> None:
        """Called when agent encounters an error."""
        print(f"\n❌ ERROR: {str(error)}")


def interactive_agent_loop(agent: ReActAgent):
    """
    Interactive loop that shows the agent's thinking process and tool usage.
    Educational for beginners to understand how the agent works.
    
    Args:
        agent (ReActAgent): The agent to run in interactive mode
    """
    print("\n===== IoT Agent Interactive Mode =====")
    print("Type '/exit' to quit\n")
    
    while True:
        # Get user input
        user_input = input("\n🧠 Ask the agent: ")
        if user_input.strip().lower() == '/exit':
            print("Exiting interactive mode...")
            break
            
        print("\n==== AGENT THINKING PROCESS ====")
        
        # Create a callback to capture and display the agent's thinking
        callback = VerboseCallback()
        callback_manager = CallbackManager([callback])
        agent.callback_manager = callback_manager
        
        # Run the agent with verbose output
        response = agent.chat(user_input)
        
        print(f"\n✅ FINAL RESPONSE:\n{response}")
        print("\n==== END OF PROCESS ====")
