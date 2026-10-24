"""A tiny company handbook and questions about it. Don't edit this file."""
import re

HANDBOOK = """Leave policy

Every full-time employee gets 24 days of paid leave a year. Interns get 8 casual leaves for the whole internship. Leave that is not used by 31 March does not carry over, except for up to 5 days that can be moved to the next year with your manager's approval.

Sick leave is separate from paid leave. You can take up to 12 sick days a year. For more than 2 sick days in a row, share a doctor's note with HR within a week of returning.

Parental leave is 26 weeks for the birth parent and 4 weeks for the other parent. It can be taken any time in the first year after the child arrives.

Work from home

Everyone can work from home on Mondays and Fridays. Fully remote work needs approval from your skip-level manager and is reviewed every 6 months. The company pays up to Rs 15,000 once for a home office setup, against bills submitted within 60 days of joining.

Your laptop must use full-disk encryption and the company VPN when you open internal tools from outside the office. Public Wi-Fi without the VPN is never allowed.

Expenses

Travel for work is booked through the travel desk, not by you. Economy class is the default for flights under 6 hours. Hotel stays are capped at Rs 6,000 a night in metro cities and Rs 4,000 elsewhere.

Meals while travelling are covered up to Rs 1,200 a day without receipts. Anything above that needs receipts. Submit every expense claim within 30 days of the trip, or it will not be paid.

Learning

Each employee has a learning budget of Rs 50,000 a year for courses, books and conferences. Certifications count, but the exam fee is paid only once even if you retake it. Ask your manager before you spend more than Rs 10,000 at a time.
"""

QUESTIONS = [
    ("How many casual leaves do interns get?", "8 casual leaves"),
    ("How many paid leave days carry over to next year?", "up to 5 days"),
    ("When do I need a doctor's note for sick leave?", "more than 2 sick days in a row"),
    ("How long is parental leave for the birth parent?", "26 weeks"),
    ("Which days can I work from home?", "Mondays and Fridays"),
    ("How much does the company pay for a home office?", "Rs 15,000"),
    ("Can I use public Wi-Fi for internal tools?", "Public Wi-Fi without the VPN is never allowed"),
    ("What is the hotel limit in metro cities?", "Rs 6,000 a night"),
    ("How long do I have to submit an expense claim?", "within 30 days of the trip"),
    ("What is the yearly learning budget?", "Rs 50,000 a year"),
]

STOP = {"a", "an", "the", "is", "are", "do", "i", "for", "to", "of", "how", "what", "which", "when", "can", "my", "in", "does", "much", "many", "long", "have", "need", "use"}


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP}


def score(query: str, chunk: str) -> float:
    """A simple keyword score: how many of the query's words appear in the chunk."""
    return len(words(query) & words(chunk))
