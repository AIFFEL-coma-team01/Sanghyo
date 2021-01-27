'''
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

인덱스m 에서 n까지를 역순으로 만들기
인덱스m 은 1부터 시작
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #예외 처리
        if not head or m == n:
            return head

        root = start =ListNode(None)
        root.next =head

        #start, end 저장
        for _ in range(m - 1):
                start = start.next
        end = start.next

        #반복 처리 (노드 뒤집기)
        for _ in range (n -m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

s = Solution()
l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(None))))))
m = 2
n = 4
print(s.reverseBetween(l1,m,n))