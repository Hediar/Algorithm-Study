import sys

n, m = map(int, sys.stdin.readline().split())
d = {}

for i in range(n):
    a = sys.stdin.readline().rstrip()
    d[i+1] = a  # 숫자를 key로
    d[a] = i+1  # 포켓몬 이름을 key로
# print(d)

for _ in range(m):  # 문제
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(d[int(problem)])
    else:
        print(d[problem])
