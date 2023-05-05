import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    q.append(i+1)

for j in range(len(q)-1):
    q.popleft()
    num = q.popleft()
    q.append(num)

result = q.pop()
print(result)
