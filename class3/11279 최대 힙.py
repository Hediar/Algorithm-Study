import sys
import heapq

input = sys.stdin.readline
n = int(input())

max_heap = []

for i in range(n):
    num = int(input())
    if num != 0: # 숫자일 때 추가연산
        heapq.heappush(max_heap, (-num))
        
    else: 
        if max_heap: # 값이 있을 때, 제거 
            print(-1 * heapq.heappop(max_heap))
        else:
            print(0)