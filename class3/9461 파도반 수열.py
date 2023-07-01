"""
- 입력
    테스트 케이스 T
    정수 N
    
- 출력
    P(N) → n번째 파도판 수열의 가장 긴 변의 길이
"""

import sys
input = sys.stdin.readline
# 1<= n <= 100
P = [0 for i in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
    P[i] = P[i-3] + P[i-2]

T = int(input())

for _ in range(T):
    n = int(input())
    print(P[n])
