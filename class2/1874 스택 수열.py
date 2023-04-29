n = int(input())

stack = []
result = []
cnt = 1

for i in range(n):
    num = int(input())
    # 입력한 수를 만날 때 까지 1부터 append
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))
