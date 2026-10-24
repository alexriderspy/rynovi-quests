"""20 copilot runs: the tools a good run uses (in order), what the agent actually called, and whether it finished the task.
Don't edit this file."""

RUNS = [
    {'run': 'r01', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'book_slot'], 'success': True},
    {'run': 'r02', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'search_manuals', 'search_manuals', 'search_manuals', 'search_manuals', 'check_policy', 'issue_refund'], 'success': True},
    {'run': 'r03', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['send_email'], 'success': False},
    {'run': 'r04', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'book_slot', 'lookup_customer'], 'success': True},
    {'run': 'r05', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'check_policy', 'issue_refund'], 'success': True},
    {'run': 'r06', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['search_manuals'], 'success': True},
    {'run': 'r07', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'search_manuals', 'search_manuals', 'search_manuals', 'search_manuals', 'check_calendar', 'book_slot'], 'success': True},
    {'run': 'r08', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'check_policy', 'send_email'], 'success': False},
    {'run': 'r09', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['search_manuals', 'lookup_customer'], 'success': True},
    {'run': 'r10', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'book_slot'], 'success': True},
    {'run': 'r11', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'check_policy', 'issue_refund'], 'success': True},
    {'run': 'r12', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['search_manuals', 'search_manuals', 'search_manuals', 'search_manuals', 'search_manuals'], 'success': True},
    {'run': 'r13', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'send_email'], 'success': False},
    {'run': 'r14', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'check_policy', 'issue_refund', 'lookup_customer'], 'success': True},
    {'run': 'r15', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['search_manuals'], 'success': True},
    {'run': 'r16', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'book_slot'], 'success': True},
    {'run': 'r17', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'search_manuals', 'search_manuals', 'search_manuals', 'search_manuals', 'check_policy', 'issue_refund'], 'success': True},
    {'run': 'r18', 'task': 'answer_faq', 'expected_tools': ['search_manuals'], 'steps': ['send_email'], 'success': False},
    {'run': 'r19', 'task': 'book_visit', 'expected_tools': ['lookup_customer', 'check_calendar', 'book_slot'], 'steps': ['lookup_customer', 'check_calendar', 'book_slot', 'lookup_customer'], 'success': True},
    {'run': 'r20', 'task': 'refund', 'expected_tools': ['lookup_order', 'check_policy', 'issue_refund'], 'steps': ['lookup_order', 'check_policy', 'issue_refund'], 'success': True},
]
