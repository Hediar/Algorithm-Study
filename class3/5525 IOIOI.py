"""
- 입력
    N: O의 개수
    M: S의 길이
    S: I,O로만 이루어진 문자열 
    
- 출력
    S에 Pn이 몇군데 포함되어있는지

- 접근법
    연속으로 문자열 S가 나온다면 +1을 카운트 해준다.
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

cnt = 0
i = 1
ans = 0

while i < M-1:  # 1 ~ M-1
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        cnt += 1
        i += 2  # 이미 처리된 문자 건너뛰기
    # N 은 IOI의 개수니까 cnt가 N과 같으면 1번 나온 것과 같다.
        if cnt == N:
            ans += 1
            cnt -= 1

    else:
        i += 1
        cnt = 0


print(ans)
