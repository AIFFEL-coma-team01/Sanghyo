'''
Given an integer array nums of 2n integers, 
group these integers into n pairs (a1, b1), (a2, b2), ..., 
(an, bn) such that the sum of min(ai, bi) for all i is maximized. 
Return the maximized sum.

n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하시오
예)
Input: nums = [1,4,3,2]
Output: 4

'''

# def arrayPairSum(self, nums: List[int]) -> int:
def arrayParisum(self,nums)):
    sum = 0
    pair = []
    nums.sort()

    for i in nums:

        pair.append(i)
        

