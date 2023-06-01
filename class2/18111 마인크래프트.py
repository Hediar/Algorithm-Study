import sys

# 입력 구간
N, M, B = map(int, sys.stdin.readline().split())  # 세로 가로, 인벤토리에 있는 블록 개수
ground = []
for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))
# print(ground)
min_h = min(min(ground))
max_h = max(max(ground))

# print(min_h, max_h)
res = [1e9, 0]  # 최종 시간(무한대로 초기화)과 최종 높이 저장

for v in range(min_h, max_h + 1):
    up = 0  # 높이가 v보다 작은 지형에서 필요한 블록의 개수 저장
    down = 0  # 반대로 높은 지형에서 제거할 블록의 개수 저장
    time = 0

    for i in range(N):
        for j in range(M):
            diff = ground[i][j] - v
            if diff > 0:
                down += diff
            else:
                up -= diff

    if down + B >= up:
        time = down * 2 + up  # 총 시간
        if res[0] >= time:  # 최소 시간 갱신
            res[0] = time
            res[1] = v  # 최소시간일 때의 현재 높이

print(*res)  # 각 요소를 공백으로 구분하여 출력
