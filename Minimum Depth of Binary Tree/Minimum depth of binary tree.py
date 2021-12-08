from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0

    # Initial depth is 1 if we have valid root
    depth = 1
    # Creates a deque for storing nodes from each level, so we could check every one of them from left to right
    level = deque()
    level.append(root)
    while level:
        levelSize = len(level)
        for _ in range(levelSize):
            current = level.popleft()
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)

            # if there is no left and right node to the current node - we found our minimum depth
            if not current.left and not current.right:
                return depth
        # Increment depth if we there was no ending nodes on this level
        depth += 1
