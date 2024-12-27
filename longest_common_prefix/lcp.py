from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # Iterate through the first string
        # strs = ["flower", "flow", "flight"]
        for i in range(len(strs[0])):
            # Iterate through all the strings
            for s in strs:
                # If i is the length of any of the strings, return res
                # For instance, the loop stops when i = 4 because flow is 4 characters
                '''
                Another example, the loop stops at s[2] because the first string is "o",
                but the third string is "i" which does not match that character. Therefore,
                s[2] != strs[0][2] because s[2] = "i" and strs[0][2] = "o". Return res.
                '''
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # Algorithm keeps running to add the next character.
            res += strs[0][i]
        return res

# Test Harness

def test():
    solution = Solution()

    test_cases = [
        {"strs": ["flower", "flow", "flowers"], "expected": "flow"},
        {"strs": ["apple", "app", "ape"], "expected": "ap"},
    ]

    for i, test in enumerate(test_cases):
        strs = test["strs"]
        expected = test["expected"]
        result = solution.longestCommonPrefix(strs)
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

if __name__ == "__main__":
    test()