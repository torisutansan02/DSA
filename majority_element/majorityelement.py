from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize res and count to 0
        res, count = 0, 0

        for n in nums:
            # If the count is = 0, the res = n
            # nums = [3, 2, 3]
            # First iteration, count = 0 and therefore res = n which res = 3.
            # Second iteration, count = 1. Keep res = 3.
            # Third iteration, count = 0. Keep res = 3.
            if count == 0:
                res = n
            
            # count += 1 if n == res which n = 3 and res = 3, so count = 1.
            # count -= 1 because n = 2 and res = 3. Therefore, count = 0.
            # count += 1 if n == res which n = 3 and res = 3, so count = 1.
            count += (1 if n == res else -1)

        return res
    
# Test Harness
def test():
    solution = Solution()
    
    test_cases = [
        {"nums": [3, 2, 3], "expected": 3},
        {"nums": [1, 2, 2, 1, 1, 1, 1, 1, 2, 2], "expected": 1},
    ]

    for i, test in enumerate(test_cases):
        nums = test["nums"]
        expected = test["expected"]
        result = solution.majorityElement(nums)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

if __name__ == "__main__":
    test()