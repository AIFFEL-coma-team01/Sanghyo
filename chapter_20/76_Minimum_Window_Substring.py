
'''
76. Minimum Window Substring
Given two strings `s` and `t`, return the minimum window in `s` which will contain all the characters in `t`. 
If there is no such window in `s` that covers all characters in `t`, return the empty string "".

두 개의 문자열 s와 t가 주어지면 t의 모든 문자를 포함 할 s의 최소 창을 반환합니다. 
s에 t의 모든 문자를 포함하는 창이 없으면 빈 문자열 ""을 반환합니다

Note: that If there is such a window, it is guaranteed that there will always be only one unique minimum window in `s`.
그러한 기간이있는 경우 s에는 항상 고유 한 최소 기간이 하나만 있음이 보장됩니다.

 
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:

Input: s = "a", t = "a"
Output: "a"


'''
# <76_부분 문자열이 포함된 최소 윈도우>

# 문자열 S와 T를 입력받아 O(n) 에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라


# 부분 문자열이 포함된 최소 윈도우 

# T = ABC =>3개의 문자이므로
# 윈도우 사이즈를 3으로 한 뒤 끝까지 스캔 
# T 에 해당 하는 문자열을 발견하지 못한 경우 4, 5, 6으로 크기를 늘리는 방법을 고려 
# time복잡도 = O(n)의 제한이 있으므로 유의
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
'''        

class Soulution(Object):
    def minWindow(self, s: str, t: str) -> str: #최소 윈도우 함수 선언
        def contains(s_substr_lst : List , t_lst: List): # t의 요소 하나씩 비교하며 슬라이딩 윈도우 내에 속한 문자를 제거
            for t_elem in t_lst: #입력 t의 요소가 t 리스트에 있는동안
                if t_elem in s_substr_lst: #t 요소가 s 리스트에 있으면
                    s_substr_lst.remove(t_elem) # s 리스트에서 t 요소를 제거
                else:
                    return False #아니면 False 반환
            return True

        if not s or not t:
            return '' # 만약 s 혹은 t 가 충족 되지 않을경우 빈 문자열 반환
        
        window_size = len(t) #윈도우 사이즈는 리스트 t의 길이로 설정

        for size in range(window_size, len(s) + 1): # 윈도우 사이즈 =3 , 입력리스트 s길이 (예제에서는 13) + 1 => range(3,13)
            for left in range(len(s) - size +1): # range(13 - size +1 )
                s_substr = s[left:left + size]
                if contains(list(s_substr),list(t)):
                    return s_substr
        return ''