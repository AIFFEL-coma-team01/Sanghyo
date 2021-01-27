'''
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL


Constraints:
    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].

연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하기
공간복잡도O(1) , 시간복잡도O(n)에 풀이할 것

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        #반복하면서 홀수,짝수 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next , even.next
        #홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head
s = Solution()
l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(None))))))
print(s.oddEvenList(l1))




