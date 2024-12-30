from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, - 1, -1):
            if (digits[i] < 9):
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits
    
def test():
    solution = Solution()

    test_cases = [
        {"digits": [9, 9], "expected": [1, 0, 0]}
    ]

    for i, test in enumerate(test_cases):
        digits = test["digits"]
        expected = test["expected"]
        result = solution.plusOne(digits)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

if __name__ == "__main__":
    test()