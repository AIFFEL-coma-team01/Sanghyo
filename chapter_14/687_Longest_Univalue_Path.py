'''
687. Longest Univalue Path
Given the root of a binary tree, 
return the length of the longest path, 
where each node in the path has the same value. 
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Input: root = [5,4,5,1,1,5]
Output: 2

44. 가장 긴 동일 value 경로
동일한 value를 지닌 가장 긴 경로를 찾아라
-> 트리의 말단(리프노드)까지 DFS탐색 후, value가 일치할 경우 백트래킹하여 이동 거리를 누적하며 계산
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode):
        def dfs(node: TreeNode):
            #만약 트리노드가 없다면 0을 반환
            if node is None:
                return 0

            #존재하지 않는 노드까지 DFS 재귀 탐색위한 코드 구현
            #left,right 변수 선언
            left = dfs(node.left)
            right = dfs(node.right)

            #현재 노드가 왼쪽 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            #현재 노드가 오른쪽 자식 노드와 동일한 경우 거리 1 증가    
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            #왼쪽과 오른쪽 자식 노드 가안 거리의 합 최대가압이 결과
            self.result = max(self.result, left + right)
            #max()함수를 이용하여 자식 노드 상태 가압 중 큰 가압 리턴
            return max(left, right)

        dfs(root) # 
        return self.result

# input :  
# root = [5,4,5,1,1,5]
# output : 
#2

# input :  
# root = [1,4,5,4,4,5]
# output : 
# 2
# s = Solution()
# t = TreeNode(root)
# print(s.longestUnivaluePath(t))
