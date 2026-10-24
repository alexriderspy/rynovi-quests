import json

from quests.day58.gate import drops, main, next_baseline

BASE = {"faithfulness": 0.91, "hit_rate_at_5": 0.84, "refusal_ok": 0.95}


def test_58_1_drops():
    assert drops(BASE, {"faithfulness": 0.86, "hit_rate_at_5": 0.835, "refusal_ok": 0.97}) == ["faithfulness: 0.91 -> 0.86"]
    assert drops(BASE, {"faithfulness": 0.92, "hit_rate_at_5": 0.84}) == ["refusal_ok: 0.95 -> missing"]


def test_58_2_cli(tmp_path, capsys):
    b, c = tmp_path / "b.json", tmp_path / "c.json"
    b.write_text(json.dumps(BASE))
    c.write_text(json.dumps(BASE | {"hit_rate_at_5": 0.70}))
    assert main([str(b), str(c)]) == 1
    assert "hit_rate_at_5: 0.84 -> 0.70" in capsys.readouterr().out
    c.write_text(json.dumps(BASE | {"faithfulness": 0.95}))
    assert main([str(b), str(c)]) == 0
    assert "no regressions" in capsys.readouterr().out


def test_58_3_baseline_moves_only_forward():
    better = BASE | {"faithfulness": 0.95}
    assert next_baseline(BASE, better) == better
    worse = BASE | {"faithfulness": 0.5}
    nb = next_baseline(BASE, worse)
    assert nb == BASE and nb is not BASE
