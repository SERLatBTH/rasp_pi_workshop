"""
Base tool class for the agent.
"""
from typing import Any, Dict

from llama_index.core.tools import BaseTool


class DocumentedTool(BaseTool):
    """
    Base class for tools with additional documentation.
    
    This class extends the BaseTool class from llama_index to provide
    additional documentation and structure for custom tools.
    
    To create a custom tool:
    1. Subclass this class
    2. Define a descriptive name and description
    3. Implement the __call__ method with your tool's logic
    4. Return results in a structured format
    """
    
    def __call__(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Execute the tool with the provided arguments.
        
        Args:
            **kwargs: Keyword arguments for the tool
            
        Returns:
            Dict[str, Any]: The result of the tool execution
        """
        try:
            return self._execute(**kwargs)
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }
    
    def _execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Internal method to execute the tool's logic.
        
        This method should be implemented by subclasses.
        
        Args:
            **kwargs: Keyword arguments for the tool
            
        Returns:
            Dict[str, Any]: The result of the tool execution
        """
        raise NotImplementedError("Subclasses must implement _execute method")
