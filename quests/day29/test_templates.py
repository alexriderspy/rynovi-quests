import pytest

from quests.day29.templates import chatml, check_conversation, llama3

CHAT = [
    {"role": "system", "content": "Label the issue."},
    {"role": "user", "content": "App crashes on login"},
    {"role": "assistant", "content": "bug"},
]


def test_29_1_chatml():
    assert chatml(CHAT) == (
        "<|im_start|>system\nLabel the issue.<|im_end|>\n"
        "<|im_start|>user\nApp crashes on login<|im_end|>\n"
        "<|im_start|>assistant\nbug<|im_end|>\n"
    )


def test_29_2_generation_prompt():
    out = chatml(CHAT[:2], add_generation_prompt=True)
    assert out.endswith("<|im_start|>user\nApp crashes on login<|im_end|>\n<|im_start|>assistant\n")
    assert not chatml(CHAT[:2]).endswith("assistant\n")


def test_29_3_llama3():
    assert llama3(CHAT[:2], add_generation_prompt=True) == (
        "<|begin_of_text|>"
        "<|start_header_id|>system<|end_header_id|>\n\nLabel the issue.<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n\nApp crashes on login<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|>\n\n"
    )


def test_29_4_good_conversations_pass():
    assert check_conversation(CHAT) is None
    assert check_conversation(CHAT[1:]) is None


@pytest.mark.parametrize("bad", [
    [{"role": "bot", "content": "hi"}],
    [{"role": "user", "content": "a"}, {"role": "system", "content": "late rules"}],
    [{"role": "assistant", "content": "I speak first"}],
    [{"role": "user", "content": "a"}, {"role": "user", "content": "b"}],
])
def test_29_4_bad_conversations_fail(bad):
    with pytest.raises(ValueError):
        check_conversation(bad)
