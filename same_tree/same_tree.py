from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees have no nodes, return True
        if not p and not q:
            return True
        
        # If one tree or the other tree have nodes but one does not, return False
        if not p or not q:
            return False
        
        # If the tree's values are not equal, return False
        if p.val != q.val:
            return False
        
        # Recursively check the left and right sides of the tree to see if they are the same and return true if they are
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
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

def test():
    solution = Solution()

    test_cases = [
        {"p": [1, 2, 3], "q": [1, 2, 3], "expected": True}
    ]

    for i, test in enumerate(test_cases):
        p = build_tree(test["p"])
        q = build_tree(test["p"])
        expected = test["expected"]
        result = solution.isSameTree(p, q)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"

        print(f"Test case {i + 1} passed: {result} == {expected}")

test()