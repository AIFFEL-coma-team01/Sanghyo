'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node,next = node.next , prev
            return reverse(next, node)
        return reverse(head)

s=Solution()
l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(None))))))

print(s.reverseList(l1))