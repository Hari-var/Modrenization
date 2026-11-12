from openai import AzureOpenAI  # type: ignore
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .config import Content_generator_model_config as cgconfig

SYSTEM_PROMPT = "You are a helpful assistant."
MAX_HISTORY_MESSAGES = 20  # cap so the context doesn't grow forever

# In-memory conversation store: {session_id: [{"role": ..., "content": ...}, ...]}
_sessions = {}
_client = None


def _get_client():
    """Create the Azure client once and reuse it."""
    global _client
    if _client is None:
        if not cgconfig.AI_content_key:
            raise ValueError("AI_content_key not found in config/environment")
        _client = AzureOpenAI(
            api_version=cgconfig.AI_content_version,
            azure_endpoint=cgconfig.AI_content_endpoint,
            api_key=cgconfig.AI_content_key,
        )
    return _client


def get_azure_response(text, new_session=False, session_id="default"):
    """
    Call the LLM with conversation context.

    text:        the user's message
    new_session: True -> wipe the history for this session_id and start fresh
    session_id:  lets you keep multiple independent conversations (e.g. per user)
    """
    try:
        if new_session or session_id not in _sessions:
            _sessions[session_id] = []

        history = _sessions[session_id]
        messages = history + [{"role": "user", "content": text}]

        response = _get_client().responses.create(
            model=cgconfig.AI_content_model,
            instructions=SYSTEM_PROMPT,
            input=messages,
        )

        reply = response.output_text

        # Save to history only after a successful call
        history.append({"role": "user", "content": text})
        history.append({"role": "assistant", "content": reply})
        _sessions[session_id] = history[-MAX_HISTORY_MESSAGES:]

        return reply
    except Exception as e:
        return {"Azure Error": str(e)}


if __name__ == "__main__":
    print(get_azure_response("My name is Ravi."))
    print(get_azure_response("What is my name?"))                    # remembers: Ravi
    print(get_azure_response("What is my name?", new_session=True))  # fresh: doesn't know