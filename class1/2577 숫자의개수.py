A = int(input())
B = int(input())
C = int(input())
num = A * B * C
n_list = list(map(int, str(num)))

for i in range(10):
    print(n_list.count(i))
