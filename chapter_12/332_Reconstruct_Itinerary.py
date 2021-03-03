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

'''
#DFS로 일정 그래프 구성
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collection.defaultdict(list)
        # 그래프 순서대로 구성
        for a , b in sorted(tickets):
            graph[a].append(b)
        route = []
        def dfs(a):
                # 첫 번째 가압을 읽어 어휘 순 방문
                while graph[a]:
                    dfs(graph[a].pop(0))
                route.append(a)
        dfs('JFK')
        #다시 뒤집어 어휘 순 결과로 반환
        return route[::-1]
        