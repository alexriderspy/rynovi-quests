from quests.day10.detective import INVOICES, extract_text, find_total, is_scan, line_items

DIGITAL, TABLE, SCAN = INVOICES / "digital.pdf", INVOICES / "table.pdf", INVOICES / "scan.pdf"


def test_10_1_reads_text():
    text = extract_text(DIGITAL)
    assert "Chai Point Supplies" in text and "CPS-2026-0412" in text


def test_10_1_scan_gives_empty_text():
    assert extract_text(SCAN).strip() == ""


def test_10_2_finds_the_total_not_the_subtotal():
    assert find_total(extract_text(DIGITAL)) == 12449.0
    assert find_total(extract_text(TABLE)) == 25500.5


def test_10_2_no_total():
    assert find_total("Subtotal: Rs 100.00") is None


def test_10_3_line_items():
    items = line_items(TABLE)
    assert items == [
        {"item": "GPU hours (A100)", "qty": 12, "amount": 18000.0},
        {"item": "Vector DB, monthly", "qty": 1, "amount": 4500.5},
        {"item": "Support plan", "qty": 2, "amount": 3000.0},
    ]
    assert sum(i["amount"] for i in items) == find_total(extract_text(TABLE)), "the lines should add up to the total"


def test_10_4_spots_the_scan():
    assert is_scan(SCAN) is True
    assert is_scan(DIGITAL) is False and is_scan(TABLE) is False
