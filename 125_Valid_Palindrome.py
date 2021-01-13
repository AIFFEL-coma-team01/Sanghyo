from typing import List
import re


def isPalindrome(self , s: str) -> bool:
    s = s.lower() # 소문자로 변환하여 변수에 저장
    '''
    #교체함수(매치객체)
    #re.sub('패턴', 교체함수, '문자열', 바꿀횟수)

    '''
    #a-z , 0-9, 정규표현식을 이용하여 문자와 숫자만 변수에 저장
   
    s = re.sub('[^a-z0-9]','',s) 
    
    return s == s[::-1] # 슬라이싱 -> 뒤집어진 문자열 반환

str = ['']
isPalindrome('tomot',str)