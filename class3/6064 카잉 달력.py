"""
- 입력
    T : 테스트 케이스 
    한줄 씩 : M, N, x, y

- 출력
    k : <x:y>가 k번째 해를 나타내는 것
    출력 못하면 -1 출력


"""

import sys
input = sys.stdin.readline

def kaing(M, N, x, y):
    num = x
    while num <= M * N :
        if (num - x) % M == 0 and (num - y) % N == 0:
            return num
        num += M 
    return -1

T = int(input())
for _ in range(T):
    M,N,x,y = map(int, input().split())
    print(kaing(M,N,x,y))
