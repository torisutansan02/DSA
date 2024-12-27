from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize previous map to an empty set
        prevMap = {}

        # Enumerate [i, val[i]]
        # nums = [2, 3, 1, 4], target = 7
        # for 0, 2 in enumerate(nums):
        for i, n in enumerate(nums):
            # the difference is equal to the target 7 - n
            # i = 0, n = 2. diff = 7 - 2
            diff = target - n

            # Check if the difference is in previous map.
            # if 7 in prevMap, not true for 1st iteration.
            # 4th iteration, diff = 3 in prevMap.
            if diff in prevMap:
                # Return [1, 3] in the fourth iteration
                return [prevMap[diff], i]

            # 1st iteration, prevMap[2] = 0 {2: 0}
            # 2nd iteration, prevMap[3] = 1 {3: 1}
            # Last iteration, prevMap = {2: 0, 3: 1, 1: 2, 4: 3}
            prevMap[n] = i

# Test Harness
def test_twoSum():
    solution = Solution()
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [2, 3, 1, 4], "target": 7, "expected": [1, 3]},
        {"nums": [1, 2, 3, 4, 5], "target": 8, "expected": [2, 4]},
    ]

    for i, test in enumerate(test_cases):
        nums = test["nums"]
        target = test["target"]
        expected = test["expected"]
        result = solution.twoSum(nums, target)
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

# Run the tests
if __name__ == "__main__":
    test_twoSum()