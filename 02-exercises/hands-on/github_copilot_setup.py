# Option 1: GitHub Copilot (local API proxy) setup
# Run this cell if you don't have CircuIT access
# Make sure you have followed the setup steps in GitHub-Copilot-2-API/README.md first

import warnings
warnings.filterwarnings('ignore')

import anthropic
from typing import Any, List

def _extract_text_from_blocks(blocks: List[Any]) -> str:
    """Extract text content from response blocks returned by the API."""
    parts: List[str] = []
    for block in blocks:
        text_val = getattr(block, "text", None)
        if isinstance(text_val, str):
            parts.append(text_val)
        elif isinstance(block, dict):
            t = block.get("text")
            if isinstance(t, str):
                parts.append(t)
    return "\n".join(parts)

# This function handles communication with the GitHub Copilot API proxy
# Select the appropriate model from those available through the proxy server
def get_chat_completion(messages, model="claude-sonnet-4", temperature=0.0):
    client = anthropic.Anthropic(
        api_key="dummy-key",  # not used by local proxy
        base_url="http://localhost:7711"
    )
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        temperature=temperature
    )
    return _extract_text_from_blocks(getattr(response, "content", []))

print("✅ GitHub Copilot API setup complete! Ready for activities.")