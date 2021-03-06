'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

연결리스트를 입력받아 페어 단위로 스왑하


Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
Example 2:
    Input: head = []
    Output: []
Example 3:
    Input: head = [1]
    Output: [1]
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


Follow up: Can you solve the problem without modifying the values in the list's nodes?
(i.e., Only nodes themselves may be changed.)


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

s = Solution()
head = [1,2,3,4]
print(s.swapPairs(head))