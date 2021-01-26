'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셉 결과가 되도록 출력하다

예)

입력
list = [1,2,3,4]

list2[0] =  list[1] * list[2] * list[3]

출력
list2 = [24,12,8,6]

'''
def productExceptSelf(num)
    nums = []
    for i in range(len(nums)
        nums = (num-num[i])
