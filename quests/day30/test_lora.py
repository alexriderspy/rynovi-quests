import numpy as np

from quests.day30.lora import LoRALinear, full_params, lora_budget, lora_params

rng = np.random.default_rng(42)
W = rng.normal(size=(64, 32))
X = rng.normal(size=(5, 32))


def test_30_1_counting():
    assert full_params(4096, 4096) == 16_777_216
    assert lora_params(4096, 4096, 8) == 65_536
    assert lora_params(32, 64, 4) == 4 * (32 + 64)


def test_30_2_shapes():
    layer = LoRALinear(W, r=4, alpha=8)
    assert layer.A.shape == (4, 32) and layer.B.shape == (64, 4)
    assert np.all(layer.B == 0), "B must start at zero"
    assert np.abs(layer.A).max() < 0.1, "A should be small random numbers (normal × 0.01)"


def test_30_2_starts_as_a_no_op():
    layer = LoRALinear(W, r=4, alpha=8)
    assert np.allclose(layer.forward(X), X @ W.T), "a fresh LoRA layer must give exactly the original output"


def test_30_3_merge_matches_forward():
    layer = LoRALinear(W, r=4, alpha=8)
    layer.B = rng.normal(size=layer.B.shape)  # pretend we trained it
    assert not np.allclose(layer.forward(X), X @ W.T), "once B is trained, the output should change"
    assert np.allclose(X @ layer.merged().T, layer.forward(X))


def test_30_4_budget_for_a_1b_model():
    # Llama 3.2 1B: 16 layers, d_model 2048. LoRA rank 8 on q_proj and v_proj.
    n = lora_budget(16, 2048, 8)
    assert n == 1_048_576
    assert n / 1_240_000_000 < 0.001, "that's under 0.1% of the model"
