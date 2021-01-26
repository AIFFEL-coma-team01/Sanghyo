from typing import List
'''
문제정의

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

*동일한 요소(element)를 두 번 사용할 수 없다.
*리턴 순서는 관계없다.

'''

def twoSum(nums,target):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
          if nums[i]+nums[j] == target:
              return [i,j]


#1-4 

from typing import List

def twoSum2(nums,target):
    nums_map = {} #빈 딕셔너리 생성
    # 이중 for 문을 1개의 for 문으로 수정
    # enumerate() 함수 > 리스트가 있는 경우 index와 value를 전달
    for i, num in enumerate(nums): #nums에 i와 num을 조회
        if target - num in nums_map: #taget-num이 딕셔너리에 있으면
            return [nums_map[target - num], i] #딕셔너리에 target - num의 value와 index를 리턴
        nums_map[num] = i # key 와 value 를 딕셔너리에 저장 

