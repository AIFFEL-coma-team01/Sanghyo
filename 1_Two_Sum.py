from typing import List
'''
문제정의

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

*동일한 요소(element)를 두 번 사용할 수 없다.
*리턴 순서는 관계없다.

'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
          if nums[i]+nums[j] == target:
              return [i,j]

