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


'''
우선순위큐
스택 : 나중에 삽입된 요소를 먼저 추출
큐 : 가장 먼저 삽입된 요소를 먼저 추출
우선순위큐 :특정 조건에 따라 요소가 추출
    최댓값 추출 하는 조건
    최소값을 추출하는 조건 등


파이썬에서 우선순위 큐를 이용하는 방법은 PriorityQueue 클래스와 heapq클래스가 있다
    기능적으로 같고 주로 heapq를 이용하여 구현한다.
차이점은 스레드세이퍼(멀티 스레드에도 안전한 프로그래밍 개념)클래스인지 아닌지로 나뉘며
    heapq클래스는 스레드 세이프를 보장하지 않는다.
    따라서 멀티스레드 구현가 필요하다면  PriorityQueue 클래스를 사용해서 우선순위 큐를 구성해야 한다
    
    
heapq(힙큐)클래스
    - 특정한 규칙을 가지는 트리구조로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다.
    - 힙 property : A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다
    - 최소 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
    - 최대 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙  
    - 이러한 특성으로 힙에서는 가장 낮은 혹은 높은 우선순위를 지니는 노드가 항상 루트에 오게 되므로
    - 우선순위 큐와 같은 추상적 자료형을 구현할수 있다.
    
    힙 함수 활용하기
        heapq.heappush(heap, item) : item을 heap에 추가
        heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
        heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
        
        - 최소 힙 Min Heap을 지원 -> lst.val이 작은 순서대로 pop()할수 있다
            - 하지만 중복된 값을 넣을 수는 없다
            e.g)
            for lst in lists:
                heapq.heappush(heap, (lst.val, lit))
           
            - 예제로 제시한 연결리스트는 첫번째와 두번째 루트가 각 1로 동일한 중복값이 존재한다.
            e.g2)
            for i in range(len(lists)):
            ...
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
    출처 : https://littlefoxdiary.tistory.com/3
'''


import heapq
# heap = []
# heapq.heappush(heap, 50)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)
#
# print(heap)
# result : [10, 20, 50]

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) #중복값 에러 방지

        #힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap) # heappop()으로 가장작은노드의 연결리스트부터 차례대로 꺼내온
            idx = node[1]
            result.next = node[2]
        #가장 작은 노드가 항상 차례대로 나올 수 있도록 추출한 연결 리스트의 그 다음 노드는 같이 다시 힙에 추가한다
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next


# Runtime: 28 ms

