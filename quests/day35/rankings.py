"""For 10 queries: the right document, and the top 7 from a keyword search (BM25) and from an embedding search.
Don't edit this file."""

QUERIES = [
    {'query': 'error code XJ-204 on checkout', 'relevant': 'D00', 'bm25': ['D00', 'D09', 'D04', 'D07', 'D06', 'D16', 'D17'], 'dense': ['D02', 'D14', 'D11', 'D19', 'D00', 'D10', 'D15']},
    {'query': 'refund for order #88123', 'relevant': 'D02', 'bm25': ['D02', 'D12', 'D05', 'D10', 'D01', 'D08', 'D00'], 'dense': ['D17', 'D15', 'D04', 'D03', 'D02', 'D14', 'D11']},
    {'query': 'GST number on invoices', 'relevant': 'D04', 'bm25': ['D04', 'D15', 'D05', 'D03', 'D01', 'D06', 'D18'], 'dense': ['D11', 'D13', 'D14', 'D07', 'D04', 'D12', 'D19']},
    {'query': 'API key rotation steps', 'relevant': 'D06', 'bm25': ['D06', 'D01', 'D04', 'D08', 'D12', 'D00', 'D11'], 'dense': ['D15', 'D05', 'D17', 'D07', 'D06', 'D16', 'D19']},
    {'query': 'Section 4.2 data retention', 'relevant': 'D08', 'bm25': ['D08', 'D02', 'D15', 'D09', 'D00', 'D17', 'D05'], 'dense': ['D01', 'D12', 'D04', 'D10', 'D08', 'D14', 'D19']},
    {'query': "my payment didn't go through", 'relevant': 'D10', 'bm25': ['D12', 'D08', 'D03', 'D07', 'D10', 'D02', 'D18'], 'dense': ['D10', 'D16', 'D17', 'D01', 'D15', 'D13', 'D06']},
    {'query': 'how do I get my money back', 'relevant': 'D12', 'bm25': ['D07', 'D10', 'D14', 'D16', 'D12', 'D11', 'D05'], 'dense': ['D12', 'D06', 'D03', 'D17', 'D08', 'D18', 'D19']},
    {'query': 'can someone else use my account', 'relevant': 'D14', 'bm25': ['D00', 'D17', 'D07', 'D02', 'D14', 'D11', 'D05'], 'dense': ['D14', 'D16', 'D09', 'D10', 'D06', 'D08', 'D13']},
    {'query': 'the app is really slow today', 'relevant': 'D16', 'bm25': ['D07', 'D04', 'D01', 'D03', 'D16', 'D08', 'D14'], 'dense': ['D16', 'D13', 'D15', 'D05', 'D18', 'D06', 'D12']},
    {'query': 'stop sending me emails', 'relevant': 'D18', 'bm25': ['D13', 'D03', 'D19', 'D09', 'D18', 'D06', 'D02'], 'dense': ['D18', 'D07', 'D14', 'D04', 'D05', 'D16', 'D10']},
]
