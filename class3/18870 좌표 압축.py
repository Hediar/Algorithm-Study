import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
dic = {}

arr = sorted(set(x))

for i in range(len(arr)): # key에 값, value에 index
    dic[arr[i]] = i

for i in x:
    print(dic[i], end=' ')