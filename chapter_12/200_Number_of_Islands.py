'''
200. Number of Islands
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라
(연결되어 있는 1의 덩어리 개수를 구하라)

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

예제1)
입력
11110
11010
11000
00000

출력
1

예제2)
입력
11000
11000
00100
00011

출력
3

*실무 면접에서 화이트보드 코딩 문제로 출제된 문제라고 함

'''
#중첩 함수 미사용 

class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        #더 이상 땅이 아닌 경우 탐색 종료
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return #백트래킹 으로 빠져 나오기

        grid[i][j] = '0'

        # 동서남북 탐색
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]])->int:
        #예외 처리
        if not grid:
            return 0 #육지(1) 가 아니면, 0을 반환
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count

# 144 ms


#중첩함수 Nested Function 활용 
#DFS(깊이탐색)재귀를 이용하여 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        
        # numIslands() 함수 안에 dfs()를 중첩함수로 선언 -> 부모 함수에서 선언한 변수활용 가능 
        def dfs(i,j):    
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return #백트래킹으로 빠져나오기

            grid[i][j] = 0 # 
            
            # 동서남북 탐색
            dfs(i+1,j) # 중첩함수 미사용시 -> self.dfs(grid, i+1, j)
            dfs(i-1,j) # 중첩함수 미사용시 -> self.dfs(grid, i-1, j)
            dfs(i,j+1) # 중첩함수 미사용시 -> self.dfs(grid, i, j+1)
            dfs(i,j-1) # 중첩함수 미사용시 -> self.dfs(grid, i, j-1)

        count = 0 
        for i in range(len(grid)):#그리드 행의 크기 와 
            for j in range(len(grid[0])):#그리드 열의 크기 동안
                if grid[i][j] == '1': #육지(1)가 있다면 
                    dfs(i,j) #육지(1) 탐색 시작 
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
'''
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''
#132 ms