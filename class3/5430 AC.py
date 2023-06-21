"""
- 입력
테스트 케이스 개수 T
수행할 함수 이름 p
배열에 들어있는 수의 개수 n
배열에 들어있는 정수

- 출력
함수 수행 결과
에러 발생 시 error 출력

R: 순서를 뒤집는다.
D: 첫 번째 수를 버린다. -> 배열이 비어있는데 실행되면 에러가 발생한다.

"""
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    fnc = input().rstrip()
    m = int(input())  # 배열에 들어있는 개수
    arr = deque(input().rstrip()[1:-1].split(','))  # 대괄호 빼고 넣기
    flag = 1
    rev = 0

    if m == 0:
        arr = deque()

    for j in fnc:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if not arr:
                print('error')
                flag = 0
                break
            else:  # arr가 true, 짝수/홀수 구분
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if flag == 1:
        if rev % 2 == 0:
            print('['+','.join(arr)+']')
        else:
            arr.reverse()
            print('['+','.join(arr)+']')
