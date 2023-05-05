from collections import Counter
import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

# 산술평균
print(round(sum(num)/n))

# 중앙값
mid = len(num)//2
num.sort()
print(num[mid])

# 최빈값
c = Counter(num)
mode = c.most_common(2)  # 2번째로 작은 값을 출력해야 하니 2개를 할당해준다.
if len(mode) == 1 or mode[0][1] != mode[1][1]:  # 1개만 있거나
    print(mode[0][0])
else:  # 2개 이상일 경우
    print(mode[1][0])


# 범위
print(max(num) - min(num))
