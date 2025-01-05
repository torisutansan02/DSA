from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store the count into a hash map
        count = {}
        res = 0
        # Initialize the left pointer to 0
        l = 0
        # Initialize max frequency to 0
        maxf = 0

        # Sliding window algorithm
        for r in range(len(s)):
            # Increment the character's count at s[r]
            count[s[r]] = 1 + count.get(s[r], 0)
            # The max frequency is the max character's count or count at s[r]
            maxf = max(maxf, count[s[r]])

            # While the sliding window - max frequency is less than k
            while (r - l + 1) - maxf > k:
                # Decrement the character's count at s[l]
                count[s[l]] -= 1
                # Increment the left pointer
                l += 1
            
            # The resolution is either the current res or the biggest sliding window
            res = max(res, r - l + 1)
        
        # Return the res
        return res

def test():

    solution = Solution()

    test_cases = [
        {"s": "AABAAC", "k": 1, "expected": 5}
    ]

    for i, test in enumerate(test_cases):
        s = test["s"]
        k = test["k"]
        expected = test["expected"]
        result = solution.characterReplacement(s, k)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"

        print(f"Test case {i + 1} passed: {result} == {expected}")

test()