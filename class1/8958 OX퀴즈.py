T = int(input())
q = []
cnt = 1
result = 0

for _ in range(T):
    arr = list(input())
    result = 0
    for i in range(len(arr)):
        if i > 0 and arr[i-1] == 'O' and arr[i] == 'O':
            cnt += 1
            result += cnt
        elif arr[i] == 'O':
            cnt = 1
            result += cnt
    print(result)
