import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []

for i in range(n):
    x = int(input())
    if x != 0: # x값을 배열에 추가한다. 
        heapq.heappush(heap,(abs(x), x)) # 절댓값과 실제 값을 넣어 분류한다.
    else: # 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거한다
        if heap: 
            print(heapq.heappop(heap)[1])
        else: # 비었을 때 
            print(0)