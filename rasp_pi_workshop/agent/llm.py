"""
LLM configuration module for the agent.
"""
from llama_index.llms.ollama import Ollama


def setup_llm(
    model="your-chosen-model",
    temperature=0.7,
    max_tokens=512,
    api_base="http://localhost:11434",
    timeout=60,
):
    """
    Set up the LLM with Ollama as an OpenAI-compatible endpoint.
    
    Args:
        model (str): The model to use
        temperature (float): The temperature parameter for generation
        max_tokens (int): The maximum number of tokens to generate
        api_base (str): The base URL for the vLLM API
        
    Returns:
        Ollama: The configured LLM
    """
    return Ollama(
        model=model,
        temperature=temperature,
        max_new_tokens=max_tokens,
        base_url=api_base,
        request_timeout=timeout,
    )
