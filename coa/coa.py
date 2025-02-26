import unittest
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

class TestSolution(unittest.TestCase):
    def test_getConcatenation(self):
        solution = Solution()
        
        # Test case 1
        self.assertEqual(solution.getConcatenation([1, 2, 3]), [1, 2, 3, 1, 2, 3])
        
        # Test case 2
        self.assertEqual(solution.getConcatenation([0, 0]), [0, 0, 0, 0])
        
        # Test case 3
        self.assertEqual(solution.getConcatenation([5]), [5, 5])
        
        # Test case 4: Empty list
        self.assertEqual(solution.getConcatenation([]), [])
        
if __name__ == '__main__':
    unittest.main()
