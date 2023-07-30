import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    if student > 32:
        print(0)
        
    