from queue import Queue
n, k = map(int, input().split())
result = []
q = Queue()
# q 순서대로 입력하기
for i in range(1, n+1):
    q.put(i)


# 큐가 비어있을 때 까지
while not q.empty():
    # k-1번씩 돌리기
    for i in range(k):
        num = q.get()  # 큐의 맨 앞 자료를 제거하고

        if i == k-1:
            result.append(num)  # i가 k-1번째라면 결과값에 숫자넣기
        else:
            q.put(num)  # 아니라면 큐의 맨 뒤에 다시 넣기

print('<', end="")
for i in range(len(result)-1):
    print("%d, " % result[i], end="")
print(result[-1], end="")
print(">")
