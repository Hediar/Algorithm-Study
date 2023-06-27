"""
- 입력
    T: 테스트 케이스
    k: 연산의 개수
    k줄 마다: 연산 문자, 정수 n
    
- 출력
    남아있는 값 중 최댓값, 최솟값
    비어있다면 EMPTY

연산
- 제거

- 삽입
    
"""
import sys
import heapq
input = sys.stdin.readline

T = int(input())
import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input()) #연산횟수
    maxHeap = [] #최대 힙
    minHeap = [] #최소 힙
    check = [False]*k #체크(최대 k번 push)
    for idx in range(k):
        op, n = input().rstrip().split()
        n = int(n)

        if op == "I": #push
            heapq.heappush(maxHeap, (-n, idx)) #최대 힙 push
            heapq.heappush(minHeap, (n, idx)) #최소 힙 push
            check[idx] = True

        elif not maxHeap or not minHeap: #비어있다면 무시
            pass

        elif n == -1: #최솟값 삭제
            #check한 원소가 True일 때까지 삭제
            while minHeap and not check[minHeap[0][1]]:
                heapq.heappop(minHeap)

            # 체크에 뺄 원소 False로 바꾸고 pop
            if minHeap:
                check[minHeap[0][1]] = False
                heapq.heappop(minHeap)

        else: #최댓값 삭제
            # check한 원소가 True일 때까지 삭제
            while maxHeap and not check[maxHeap[0][1]]:
                heapq.heappop(maxHeap)

            # 체크에 뺄 원소 False로 바꾸고 pop
            if maxHeap:
                check[maxHeap[0][1]] = False
                heapq.heappop(maxHeap)

    # 마지막으로 check
    while minHeap and not check[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not check[maxHeap[0][1]]:
        heapq.heappop(maxHeap)

    if not maxHeap or not minHeap: #비어있을 경우
        print("EMPTY")
    else: #최댓값, 최솟값 출력
        print(-maxHeap[0][0], minHeap[0][0])

# for i in range(T):
#     min_heap = [] # 최소힙
#     max_heap = [] # 최대힙
#     nums = dict()

#     k = int(input())

#     for j in range(k):
#         a,b = input().split() # 연산 문자, 정수 
#         num = int(b)

#         if a == 'I':
#             if num in nums:
#                 nums[num] += 1
#             else:
#                 nums[num] = 1
#                 heapq.heappush(min_heap, num)
#                 #기본적으로 최소힙은 작을수록 우선순위가 높기에 - 
#                 heapq.heappush(max_heap, -num) 

        
#         elif a == 'D': # 삭제 연산

#             # 비어있지 않을 때 수행
#             # 최소힙, 최대힙 둘 다 같은 값이 들어있으니 제거 
#             # 1 일 경우 최대힙 기준
#             # -1 일 경우 최소힙 기준
#             if num == -1:
#                 if min_heap:
#                     temp = heapq.heappop(min_heap)
#                     if temp in nums:
#                         del(nums[temp])
                
#                 else:
#                     print('EMPTY')
#                     break
#                 nums[min_heap[0]] -= 1

#             elif num == 1:
#                 if max_heap:
#                     temp = heapq.heappop(max_heap)
#                     if temp in nums:
#                         del(nums[temp])
#                 else:
#                     print('EMPTY')
#                     break
#                 nums[max_heap[0]] -= 1
            

            
            
