"""
입력: 회의 수 N
회의 정보 - 시작시간, 끝나는 시간 

출력: 최대 사용가능한 회의의 개수 
"""

import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = time[0][1]

for i in range(1, N):
    if time[i][0] >= end:
        cnt += 1
        end = time[i][1]

print(cnt)
