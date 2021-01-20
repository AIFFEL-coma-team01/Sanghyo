from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {} #빈 딕셔너리 생성
    # 이중 for 문을 1개의 for 문으로 수정
    # enumerate() 함수 > 리스트가 있는 경우 index와 value를 전달
    for i, num in enumerate(nums): #nums에 i와 num을 조회
        if target - num in nums_map: #taget-num이 딕셔너리에 있으면
            return [nums_map[target - num], i] #딕셔너리에 target - num의 value와 index를 리턴
        nums_map[num] = i # key 와 value 를 딕셔너리에 저장 