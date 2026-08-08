def solve (s: str) -> bool:
   cleaned = s.lower ().replace(" ","")
   return cleaned == cleaned [::-1]


TEST_CASES = [
    {"input" : {"s":"level"}, "expected": True},
    {"input" : {"s":"hello"}, "expected": False},
    {"input" : {"s":"A man a plan a canal panama"}, "expected": True},
]