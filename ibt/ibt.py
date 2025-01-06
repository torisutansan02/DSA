from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the children
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

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

# Helper function to convert a binary tree to a list (level-order traversal)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for a clean representation
    while result and result[-1] is None:
        result.pop()

    return result

def test():
    solution = Solution()

    test_cases = [
        {"root": [1, 2, 3], "expected": [1, 3, 2]},
        {"root": [4, 2, 7, 1, 3, 6, 9], "expected": [4, 7, 2, 9, 6, 3, 1]},
        {"root": [], "expected": []},
    ]

    for i, test in enumerate(test_cases):
        root = build_tree(test["root"])
        expected = test["expected"]
        result_tree = solution.invertTree(root)
        result = tree_to_list(result_tree)

        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

test()
