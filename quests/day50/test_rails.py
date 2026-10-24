import pytest

from quests.day50.rails import Budget, BudgetExceeded, check_draft, redact


def test_50_1_redact():
    assert redact("Aadhaar 1234 5678 9012, PAN ABCDE1234F") == "Aadhaar [AADHAAR], PAN [PAN]"
    assert redact("call +91 9876543210 or 09876543210") == "call [PHONE] or [PHONE]"
    assert redact("mail riya.s@example.co.in now") == "mail [EMAIL] now"
    assert redact("aadhaar 123456789012") == "aadhaar [AADHAAR]"
    assert redact("Order ORD-1042 costs Rs 1200") == "Order ORD-1042 costs Rs 1200"


def test_50_2_budget():
    b = Budget(max_steps=3, max_cost_rs=100)
    for _ in range(3):
        b.charge(1)
    with pytest.raises(BudgetExceeded, match="steps"):
        b.charge(1)
    b = Budget(max_steps=10, max_cost_rs=5)
    b.charge(3)
    with pytest.raises(BudgetExceeded, match="cost"):
        b.charge(2.5)


def test_50_3_check_drafts():
    assert check_draft("Sorry for the delay, your refund is being processed.") == []
    assert check_draft("We guarantee a 100% refund to riya@example.com") == [
        "contains personal data", "promises: guarantee", "promises: 100% refund"]
