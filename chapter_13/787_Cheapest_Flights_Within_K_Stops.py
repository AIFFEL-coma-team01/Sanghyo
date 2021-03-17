'''
There are n cities connected by m flights. 
Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. 
If there is no such route, output -1.


Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
'''
from collections import deque

class Solution(object):
    def findCheapestPrice(self, n, flight, src, dst, K):
        adj = [[] for i in xrange(n)]
        for s, e, w in flight:
            adj[s].append([e,w])
        dist = [float('inf') for i in xrange(n+1)]
        dist[src] = 0
        q = deque()
        q.append([src, 0, 0])
        while q:
            her, cost, k_count = q.popleft()
            if k_count > K:
                continue
            for i in xrange(len(adj[here])):
                there = adj[here][i][0]
                nextdist = cost + adj[here][i][1]
                if dist[there] > nextdist:
                    dist[there] = nextdist 
                    q.append([there, nextdist, k_count +1])
        return dist[dst] if dist[dst]!= float ('int') else -1

s = Solution()
n = 3
flight = [[0,1,100], [1,2,100], [0,2,500]]
src = 0
dst = 2
K = 0 
s.findCheapestPrice(n,flight,src,dst,K)        