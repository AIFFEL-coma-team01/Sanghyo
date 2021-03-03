'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

- If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
    -유효한 여행 일정이 여러 개일 경우 단일 문자열로 읽을 때 어휘 순서가 가장 작은 여행 일정을 반환해야 합니다.
- For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    -예를 들어 [JFK", "LGA] 여행 일정은 [JFK", "LGB]보다 어휘 순서가 작습니다.
- All airports are represented by three capital letters (IATA code). 
    - 모든 공항은 세 개의 대문자로 표시됩니다(IATA 코드).   
- You may assume all tickets form at least one valid itinerary.
    -하나 이상의 유효한 여행 일정에 대해 모든 항공권을 가정할 수 있습니다.
- One must use all the tickets once and only once.
    -모든 표를 사용하되 한번만 사용할 수 있습니다

[from, to] 로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라
여러 일정이 있는 경우 사전 어휘 순 Lexical Order으로 방문한다

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]


Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

collections.defalutdict()
    dictionary와 유사한 객체를 반환합니다. 
    defaultdict내장 클래스의 하위 dict클래스입니다. 
    하나의 메서드를 재정의하고 하나의 쓰기 가능한 인스턴스 변수를 추가합니다. 
    나머지 기능은 dict클래스와 동일하며 여기에 설명되어 있지 않습니다.

    첫 번째 인수는 default_factory 속성 의 초기 값을 제공 합니다. 기본 value는 None입니다. 
    나머지 모든 인수는 dict키워드 인수를 포함 하여 생성자에 전달 된 것처럼 동일하게 처리 됩니다.
https://docs.python.org/3/library/collections.html#collections.defaultdict
'''

#DFS로 일정 그래프 구성
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성하기
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        '''
        1. 그래프를 구성하고 
        for a, b in tickets:
            graph[a].append(b)
        2. 그래프를꺼내 정렬하는 방식
        for a in graph:
            graph[a].sort()
        '''
        #sorted() 함수를 활용하여 위 과정을 함축
        for a , b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
                # 첫 번째 value를  읽어 어휘 순으로 방문하기 위해 pop()함수 이용하여 재귀호출 -> 결과리스트에 역순으로 담기고, 한번 호출한 경로는 사라진다.
                while graph[a]:
                    dfs(graph[a].pop(0))
                route.append(a)
        dfs('JFK')
        #역순으로 담긴 경로를 다시 뒤집어 어휘 순 결과로 변환
        return route[::-1]
#72 ms