from collections import deque

T = int(input())
for i in range(T):
    n, m = map(int, input().split())  # 문서의 개수 n, 궁금한 문서 m
    q = deque(list(map(int, input().split())))  # 문서의 중요도
    idx = deque(list(range(n)))  # index
    cnt = 0

    while q:
        if q[0] == max(q):  # 맨 앞이 중요도가 가장 높으면
            cnt += 1
            q.popleft()
            pop_index = idx.popleft()
            if pop_index == m:
                print(cnt)
        else:  # 아니라면 맨 뒤로 옮겨준다.
            q.append(q.popleft())
            idx.append(idx.popleft())
