def solve (nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num]= i
    return []


TEST_CASES = [
    {"input" : {"nums":[2,7,11,15], "target":9}, "expected": [0,1]},
    {"input" : {"nums":[3,2,4], "target":6}, "expected": [1,2]},
   
]