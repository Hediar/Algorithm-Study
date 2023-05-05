N, r, c = map(int, input().split())
cnt = 0

while N != 0:
    N -= 1

    # 1사분면
    if r < 2**N and c < 2**N:  # x, y 값이 2^N/2 보다 작은 경우
        cnt += (2**N) * (2**N) * 0
    # 2사분면
    elif r < 2**N and c >= 2**N:  # x 값은 2^N/2보다 작고 y 값은 2^N/2보다 큰 경우
        cnt += (2**N) * (2**N) * 1
        c -= (2**N)
    # 3사분면
    elif r >= 2**N and c < 2**N:  # x 값은 2^N/2보다 크고 y 값은 2^N/2보다 작은 경우
        cnt += (2**N) * (2**N) * 2
        r -= (2**N)
    # 4사분면
    else:  # x, y 값이 2^N/2 보다 큰 경우
        cnt += (2**N) * (2**N) * 3
        r -= (2**N)
        c -= (2**N)
print(cnt)
