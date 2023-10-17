from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # 结果集
        stack = [(True, root)]  # 节点缓存集

        while stack:
            truth, node = stack.pop()
            if node is None: continue  # 空节点则不再遍历
            if truth is True:           # True代表未经过, 遇到一次经过的节点说明回归了,可记录值
                stack.append((True, node.right))
                stack.append((False, node))
                stack.append((True, node.left))

                #优先级顺序为从下而上

            else:
                res.append(node.val)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

solution = Solution()
inorder_result = solution.inorderTraversal(root)
print(inorder_result)  # 输出中序遍历结果
