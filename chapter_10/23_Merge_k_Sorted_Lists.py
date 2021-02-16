'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

k개 정렬 리스트 병합
    k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하기

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''

# import collections
# d = collections.deque()

# import heapq
#
# heap = []
# heapq.heappush(heap, 50)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)
#
# print(heap)
'''
e.g)
for lst in lists:
    heapq.heappush(heap, (lst.val, lit))
e.g2)
for i in range(len(lists)):
    ...
    heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
heapq모듈은 
    - 최소 힙 Min Heap을 지원 -> lst.val이 작은 순서대로 pop()할수 있다
        - 하지만 중복된 값을 넣을 수는 없다
        - 예제로 제시한 연결리스트는 첫번째와 두번째 루트가 각 1로 동일한 중복값이 존재한다.
        
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        #힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next
