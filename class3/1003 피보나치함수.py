def f(N):
    cnt_0 = [1, 0, 1]
    cnt_1 = [0, 1, 1]
    if N >= 3:  # 3번째 까지는 알기 쉬우니 생략
        for i in range(2, N):
            cnt_0.append(cnt_0[i-1] + cnt_0[i])  # 이전에 구한 값을 활용
            cnt_1.append(cnt_1[i-1] + cnt_1[i])
    print(cnt_0[N], cnt_1[N])


T = int(input())
for _ in range(T):
    n = int(input())
    f(n)
