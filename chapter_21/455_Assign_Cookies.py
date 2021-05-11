'''
455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.


Each child i has a greed factor g[i], 
which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size s[j]. If s[j] >= g[i], 
we can assign the cookie j to the child i, 
and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1

Explanation: You have 3 children and 2 cookies. 
The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, 
you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2

Explanation: You have 2 children and 3 cookies. 
The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.


82. 쿠키부여
아이들에게 1개씩 쿠키를 나눠줘야 함
아이 child_i 마다 그리드 팩터 grid_factor g_i를 가지고 있음
g_i = 아이가 만족하는 최소 쿠키의 크기를 말함
쿠키 cookie_j는 크기 s_j를 가지고 있으며, s_j >= g_i 여야 아이가 만족하며 쿠키를 받음
최대 몇명의 아이들에게 쿠키를 줄 수 있는지 출력하시오

예 1)
입력
[1,2,3], [1,1]

출력 
>>> 1

두번째 아이부터 크기 2 이상의 쿠키가 필요 => 가지고 있는 최대 크기는 1 => 1명의 아이에게만 줄 수 있음

예 2)
입력
[1,2], [1,2,3]

출력
>>> 2
'''
#이진 검색을 활용한 방법

'''
2개의 리스트를 모두 교차 탐색하지 않고 하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾음
이후 인덱스가 현재 부여한 아이들보다 클 경우에는 이 경우 더 줄 수 있다는 조건이 충족 되므로,
줄 수 있는 아이의 수를 1명 더 늘린다
'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            # bisect() => 정렬된 리스트를 삽입 후에 다시 정렬할 필요 없도록 관리할 수 있도록 지원
            # bisect.bisect_right(a, x, lo=0, hi=len(a))
            # a에 있는 x의 기존 항목 뒤(오른쪽)에 오는 삽입 위치를 반환
            index = bisect.bisect_right(g,i)
            if index > result:
                result += 1
        return result

#136 ms

    