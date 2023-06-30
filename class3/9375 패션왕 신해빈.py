"""
- 입력
    테스트 케이스 T (최대 100)
    해빈이의 의상 개수 n
    n줄 마다 (이름 의상종류) 공백기준으로 주어진다.
    
- 출력
    알몸이 아닌 상태로 의상을 입을 수 있는 경우의 수
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    clothes = {}
    n = int(input())
    for _ in range(n):
        c_name, c_type = input().split()
        if clothes.get(c_type) == None: # 해당 종류가 없으면 새로 넣어준다.
            clothes[c_type] = set()
        clothes[c_type].add(c_name) # 있을 때에는 해당 종류에 추가해준다.

    cnt = 1
    for key in clothes.keys(): # 종류 기준으로 경우의 수를 구하기 위해 곱해준다.
        cnt *= len(clothes[key]) + 1
    print(cnt - 1) # 알몸인 경우 제외