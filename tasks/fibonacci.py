def solve (n: int) -> int:
    if n< 2 :
        return n
    a,b = 0, 1
    for _ in range (n-1):
        a,b = b, a+b
    return b


TEST_CASES = [
    {"input" : {"n":0}, "expected": 0},
    {"input" : {"n":1}, "expected": 1},
    {"input" : {"n":10}, "expected": 55},
]