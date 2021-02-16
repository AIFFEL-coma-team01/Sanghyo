'''
def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        #현재 온도가 스택 보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer = [last] = i -last
        stack.append(i)

return answer


T = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(T))
'''

# 다른 사람 풀이 -> stack은 나중에 들어온 것이 먼저 나가는 LIFO 구조이다.
# 성준님 풀이
def dailyTemperatures(T) :
    answer = [0] * len(T)                        # [0, 0, 0, 0, 0, 0, 0, 0] 을 만든다.
    stack = []                                   # stack 이라는 빈 리스트를 만든다. --> 이전 값을 비교하기 위한 리스트이다.
    for i, cur in enumerate(T) :                 # T의 리스트의 인덱스와 값을 열거한다. [0,73], [1,74] [2,75], [3,71], ~
        while stack and cur > T[stack[-1]]:      # stack안에 원소가 존재하고, cur이 T 리스트의 이전 값보다 크다면 진행
            last = stack.pop()                   # stack에서 이전 인덱스를 제거하며, 해당 인덱스는 last에 넣는다.  
            answer[last] = i - last              # answer 리스트에서 이전 인덱스에 해당하는 값을 (현재 인덱스 - 이전 인덱스)로 설정한다. 
        stack.append(i)                          # stack에 현재 인덱스를 추가해 다음 인덱스와 비교한다.
    return answer                                # answer를 리턴한다.

# 순서를 적어보자
# i=0 : 처음에 stack 안에 아무것도 없으니 while문을 돌아가지 않고 stack에 0이 입력된다.
# 현 상태 : answer = [0, 0, 0, 0, 0, 0, 0, 0], stack = [0]

# i=1 : stack 맨 뒤에 [0]이 존재, T[0]=73이며 cur=74이다. 때문에 last는 0이며 answer[0]은 1-0인 1이 된다.  
#       stack에는 아무것도 존재하지 않으며, while은 종료된다. stack에 1이 추가된다.
# 현 상태 : answer = [1, 0, 0, 0, 0, 0, 0, 0], stack = [1]

# i=2 : stack 맨 뒤에 [1]이 존재, T[1]=74이며 cur=75이다. 때문에 last는 1이며 answer[1]은 2-1인 1이 된다.  
#       stack에는 아무것도 존재하지 않으며, while은 종료된다. stack에 2가 추가된다.
# 현 상태 : answer = [1, 1, 0, 0, 0, 0, 0, 0], stack = [2]

# i=3 : stack 맨 뒤에 [2]가 존재, T[2]=75이며 cur=71이다. 때문에 while문은 돌아가지 않고 stack에는 3을 넣는다.
# 현 상태 : answer = [1, 1, 0, 0, 0, 0, 0, 0], stack = [2,3]

# i=4 : stack 맨 뒤에 [3]이 존재, T[3]=71이며 cur=69이다. 때문에 while문은 돌아가지 않고 stack에는 4를 넣는다.
# 현 상태 : answer = [1, 1, 0, 0, 0, 0, 0, 0], stack = [2,3,4]

# i=5 : stack 맨 뒤에 [4]가 존재, T[4]=69이며 cur=72이다. 때문에 last는 4이며 answer[4]는 5-4인 1이 된다. 
#       stack 맨 뒤에 [3]이 존재, T[3]=71이며 cur=72이다. 때문에 last는 3이며 answer[3]은 5-3인 2가 된다.
#       stack 맨 뒤에 [2]가 존재, T[2]=75이며 cur=72이다. while은 종료된다. stack에 5가 추가된다.
# 현 상태 : answer = [1, 1, 0, 2, 1, 0, 0, 0], stack = [2,5]

# i=6 : stack 맨 뒤에 [5]가 존재, T[5]=72이며 cur=76이다. 때문에 last는 5이며 answer[5]는 6-5인 1이 된다. 
#       stack 맨 뒤에 [2]가 존재, T[2]=75이며 cur=76이다. 때문에 last는 2이며, answer[2]는 6-2인 4가 된다.
#       stack에는 아무것도 존재하지 않으며, while은 종료된다. stack에 6이 추가된다.
# 현 상태 : answer = [1, 1, 4, 2, 1, 1, 0, 0], stack = [6]

# i=7 : stack 맨 뒤에 [6]이 존재, T[6]=76이며 cur=73이다. 때문에 while문은 돌아가지 않고 stack에는 7을 넣으며 for문이 종료된다.
# 현 상태 : answer = [1, 1, 4, 2, 1, 1, 0, 0], stack = [2,3,6,7]

    
T = [73, 74, 75, 71, 69, 72, 76, 73] #  [1, 1, 4, 2, 1, 1, 0, 0]
dailyTemperatures(T)