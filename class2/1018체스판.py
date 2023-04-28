N, M = map(int, input().split())

# 체스판 리스트로 입력받기
g = []
for i in range(N):
    g.append(input())

cnt = []  # 사각형 들이 얼마나 칠해졌는지 저장

for i in range(N-7):
    for j in range(M-7):  # 판이 8*8을 넘어가지 않도록
        w_index = 0  # 시작이 W
        b_index = 0  # 시작이 B
        for a in range(i, i+8):  # 위에 지정한 범위부터 가로세로 8
            for b in range(j, j+8):
                if (a+b) % 2 == 0:  # 짝수
                    if g[a][b] != 'W':  # B 일때
                        w_index += 1  # W 칠하는 개수
                    else:
                        b_index += 1  # B 칠하는 개수
                else:  # 홀수
                    if g[a][b] != 'W':  # B 일때
                        b_index += 1  # B 칠하는 개수
                    else:
                        w_index += 1  # W 칠하는 개수
        cnt.append(min(w_index, b_index))
print(min(cnt))
