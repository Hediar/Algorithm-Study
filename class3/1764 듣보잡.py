"""
1. 입력값 
듣도 못한 사람 N, 보도 못한 사람 M
N개 듣도 사람 이름 
N+2부터 보도 못한 사람 이름 M개 

2. 출력값
듣도 보도 못한 사람, 즉 N과 M의 교집합을 사전순으로 출력

3. 아이디어
1) set으로 교집합 찾기
2) dictionary를 만들어서 딕셔너리에 같은 key(이름)이 있으면 +1 해주기
"""


"""
# 1번 아이디어 
N, M = map(int, input().split())
a = set()
for i in range(N):
    a.add(input())

b = set()
for j in range(M):
    b.add(input())

result = sorted(list(a & b))
print(len(result))
print('\n'.join(result))
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dic = {}

for i in range(n+m):
    name = input().strip()
    # dic에 이름이 있는지 확인하기
    if name not in dic:  # 없을경우
        dic[name] = 1
    else:
        dic[name] += 1

result = []
for a, b in dic.items():
    if b == 2:
        result.append(a)
print(len(result))
print("\n".join(sorted(result)))
