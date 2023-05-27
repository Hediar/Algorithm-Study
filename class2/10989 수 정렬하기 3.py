import sys
n = int(sys.stdin.readline())
n_list = [0] * 10000  # 수에 해당하는 index를 담기 위해

for _ in range(n):
    # 입력받을 때 마다 그 수에 해당하는 인덱스에 +1을 해주어 값으로 그 수의 개수를 담는다.
    n_list[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i+1)
