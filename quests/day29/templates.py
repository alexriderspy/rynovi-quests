"""Day 29 · Chat template by hand

A chat model never sees "messages". It sees one long string with special tokens marking who speaks.
Get the format exactly right and the model behaves; get it wrong and a good model acts dumb.

A message is a dict: {"role": "system" | "user" | "assistant", "content": "..."}
Run `python quest.py 29` after each TODO.
"""

Message = dict[str, str]


def chatml(messages: list[Message], add_generation_prompt: bool = False) -> str:
    """TODO 29.1 · The ChatML format (Qwen and many others). Each message becomes:
        "<|im_start|>{role}\\n{content}<|im_end|>\\n"
    joined together with nothing in between.

    TODO 29.2 · If add_generation_prompt is True, end with "<|im_start|>assistant\\n"
    so the model knows it's its turn to speak.
    """
    raise NotImplementedError


def llama3(messages: list[Message], add_generation_prompt: bool = False) -> str:
    """TODO 29.3 · The Llama 3 format. Start with "<|begin_of_text|>", then each message is:
        "<|start_header_id|>{role}<|end_header_id|>\\n\\n{content}<|eot_id|>"
    With add_generation_prompt, end with "<|start_header_id|>assistant<|end_header_id|>\\n\\n".
    """
    raise NotImplementedError


def check_conversation(messages: list[Message]) -> None:
    """TODO 29.4 · Raise ValueError if the conversation is malformed:
      - a role other than system, user or assistant
      - a system message anywhere except first
      - after the optional system message, turns must go user, assistant, user, assistant... starting with user
    Return None if it's fine.
    """
    raise NotImplementedError
