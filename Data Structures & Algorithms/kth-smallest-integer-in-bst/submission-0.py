# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        MyLeftTree = list()
        currNode = root
        MyLeftTree.append(currNode)
        while(currNode.left != None):
            MyLeftTree.append(currNode.left)
            currNode = currNode.left
        
        while(len(MyLeftTree) != 0):
            currNode = MyLeftTree.pop()
            if (k == 1):
                return currNode.val;
            k-=1
            if (currNode.right!= None):
                MyLeftTree.append(currNode.right)
                currNode = currNode.right
                while(currNode.left != None):
                    MyLeftTree.append(currNode.left)
                    currNode = currNode.left
            