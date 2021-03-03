from typing import List

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped.


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 잇는지 계산


'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        