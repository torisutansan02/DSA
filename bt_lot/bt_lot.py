from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res

# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = collections.deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

# Test function
def test():
    solution = Solution()

    test_cases = [
        {"root": [3, 9, 20, None, None, 15, 7], "expected": [[3], [9, 20], [15, 7]]},
        {"root": [1], "expected": [[1]]},
        {"root": [], "expected": []},
        {"root": [1, 2, 3, 4, 5, 6, 7], "expected": [[1], [2, 3], [4, 5, 6, 7]]},
    ]

    for i, test in enumerate(test_cases):
        root = build_tree(test["root"])
        expected = test["expected"]
        result = solution.levelOrder(root)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

# Run the tests
test()
