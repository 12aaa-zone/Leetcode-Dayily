# Definition for singly-linked list.
from typing import Optional

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur, pre):
            if not cur: return pre          # 若当前节点cur遇到空节点,递归停止,返回前节点pre
            res = recur(cur.next, cur)      # cur递归到末节点,使res记录这个新的"头节点",执行下一句,递归开始
            cur.next = pre                  # 以cur为镜像面,开始递归镜像
            return res                      # 返回尾节点
                                            # f(n).next => f(n+).pre, 在第一次交换时生效
        # 该递归只返回原表尾节点值,即res始终不变
        return recur(head, None)


# 示例用法
# 创建一个单链表: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
# 反转链表
new_head = solution.reverseList(head)

# 输出反转后的链表
while new_head is not None:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
