'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?




'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q: List = [] # 

        if not head:
            return True

        node = head
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        #팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True

s = Solution()
l1 = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
print(s.isPalindrome(l1))


