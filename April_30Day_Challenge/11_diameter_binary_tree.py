#!/usr/bin/python3

'''
Given a binary tree, you need to compute the length of the diameter
of the tree. The diameter of a binary tree is the length of the
longest path between any two nodes in a tree. This path may or may
not pass through the root.

Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.

'''

# ******* Option 1 *********************

def __init__(self):
	self.diameter=0

def diameterOfBinaryTree(self, root):
	def diameter(root):
		if not root:
			return 0

		d1 = diameter(root.left)
		d2 = diameter(root.right)
		d = d1+d2

		if d>self.diameter:
            self.diameter=d

		return max(d1, d2)+1

	diameter(root)
	return self.diameter


# ******* Option 2 *********************

def __init__(self):
    self.diameter = 0

def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.getHeight(root)
    return self.diameter

def getHeight(self, root):
    if root:
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return max(leftHeight, rightHeight) + 1
    else:
        return 0
