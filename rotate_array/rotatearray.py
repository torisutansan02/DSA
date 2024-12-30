from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        l, r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = 0, k - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = k, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        return nums
        
def test():
    solution = Solution()

    test_cases = [
        {"nums": [5, 2, 3, 2, 1], "k": 3, "expected": [3, 2, 1, 5, 2]},
        {"nums": [5, 2, 1, 1, 2], "k": 8, "expected": [1, 1, 2, 5, 2]}
    ]

    for i, test in enumerate(test_cases):
        nums = test["nums"]
        k = test["k"]
        expected = test["expected"]
        result = solution.rotate(nums, k)
 
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

if __name__ == "__main__":
    test()