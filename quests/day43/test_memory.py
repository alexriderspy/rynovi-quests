from quests.day43.memory import MemoryStore


def test_43_1_remember_replace_forget():
    m = MemoryStore()
    m.remember("riya", "city", "Pune")
    m.remember("riya", "city", "Bengaluru")
    assert m.get("riya", "city") == "Bengaluru"
    m.forget("riya", "city")
    assert m.get("riya", "city") is None
    m.forget("riya", "nothing")


def test_43_2_recall_relevant_only():
    m = MemoryStore()
    m.remember("riya", "employer", "Swiggy")
    m.remember("riya", "preference", "python over java")
    m.remember("riya", "city", "Pune")
    m.remember("arjun", "preference", "python")
    assert m.recall("riya", "which python course should I take") == ["preference: python over java"]
    assert m.recall("riya", "jobs near pune for swiggy people", k=5) == ["employer: Swiggy", "city: Pune"]
    assert m.recall("riya", "tell me a joke") == []


def test_43_3_extract_facts():
    m = MemoryStore()
    found = m.extract("dev", "Hi! My name is Dev Sharma. I live in Pune, and I prefer short videos.")
    assert found == [("name", "Dev Sharma"), ("city", "Pune"), ("preference", "short videos")]
    assert m.get("dev", "city") == "Pune"
    assert m.extract("dev", "What's the weather?") == []


def test_43_3_newer_facts_win():
    m = MemoryStore()
    m.extract("dev", "I work at Infosys.")
    m.extract("dev", "Big news, I work at Razorpay now")
    assert m.get("dev", "employer") == "Razorpay now"
