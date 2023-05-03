m, n = map(int, input().split())

# 모든 수가 소수(T)인 것으로 초기화
p = [True] * (n+1)
# 0과 1은 소수가 아니므로 False로 설정
p[0] = p[1] = False

for i in range(2, int(n**0.5)+1):
    if p[i]:  # i가 소수인 경우
        # i의 배수들을 False로 설정
        for j in range(i*2, n+1, i):
            p[j] = False

for i in range(m, n+1):
    if p[i]:
        print(i)
