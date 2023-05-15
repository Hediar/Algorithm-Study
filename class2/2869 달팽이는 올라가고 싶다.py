import sys

a, b, v = map(int, sys.stdin.readline().split())

day = a - b


if (v-b) % day == 0:
    print((v-b) // day)
else:
    print(((v-b) // day) + 1)
