'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.


Example 1:
    Input : l1 = [1,2,4],
            l2 = [1,3,4]
    Output : [1,1,2,3,4,4]

Example 2:
    Input : l1 = [],
            l2 = []
    Output : []

Example 3:
    Input : l1 = [],
            l2 = [0]
    Output : [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

'''



#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # 2개의 리스트를 비교하여 정렬하여 합치기
        if (not l1) or (l2 and l1.val > l2.val):
            l1,l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoListsts(l1.next, l2)
        return l1

s = Solution()
l1 = ListNode(1,ListNode(2,ListNode(4)))
l2 = ListNode(1,ListNode(3,ListNode(4)))

print(s.mergeTwoLists(l1,l2))
