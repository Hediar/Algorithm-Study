k, n = map(int, input().split())
list = []
for _ in range(k):
    list.append(int(input()))

l = 1
u = max(list)

while (l <= u):
    mid = (l+u)//2
    cnt = 0
    for i in list:
        cnt += i//mid
    if cnt >= n:  # 나눴는데 cnt가 n보다 크면? 더 큰 값으로 나누어도 되겠다
        l = mid + 1
    else:  # 위 경우랑 반대일 때
        u = mid - 1
print(u)  # 랜선의 최대 길이
