# 面试题55 二叉树的深度
'''
题目一  递归公式是n = max(n左，n右) + 1
题目二  首先，书上的方法复杂了，需要重复读取节点，所以修改最后一句就好，当树不平衡是，根节点肯定不平衡。
然后用了第二种方法，是仿照后序遍历的写法，因为后序遍历先读取左右节点，然后在根节点计算左右节点的度的差就可以。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 题目一 二叉树的深度
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        return max(left, right) + 1

    # 题目二 平衡二叉树
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            return False
        return True
        # 书上是下面一行，但是如果有一个结点不平衡的话，根节点肯定不平衡
        # return self.IsBalanced(pRoot.left) and self.IsBalanced(pRoot.right)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.right = node6
node5.left = node7

a = Solution()
# print(a.TreeDepth(node1))
print(a.IsBalanced_Solution(node1))
