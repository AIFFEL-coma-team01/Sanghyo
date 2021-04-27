'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
비어 있지 않은 정수 배열이 주어지면 모든 요소는 하나를 제외하고 두 번 나타납니다. 그 하나를 찾으십시오.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
후속 조치 : 추가 메모리를 사용하지 않고 선형 런타임 복잡성으로 솔루션을 구현할 수 있나요?

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

'''

# 딱 하나를 제외하고 모든 에ㅔㄹ리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라

# 배타적 OR = XOR 을 활용한 문제풀이
# 0 0 = 0
# 0 1 = 1
# 1 1 = 1
# 1 1 = 0

# 입력이 서로 다르면 True
# 입력이 서로 동일하면 False
# 따라서, 배열의 모든 요소를 XOR연산 하면 한번만 등장하는 요소만 남게 됨

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
#96 ms

'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0

        while (i<len(nums)):
            if len(nums)==1:
                return nums[i]
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
                nums.remove(nums[i])
                #print(nums)
            else:
                return nums[i]
'''

        