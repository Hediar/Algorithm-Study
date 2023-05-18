T = int(input())
for _ in range(T):
    check = list(input())
    stack = []
    for i in check:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:  # 비어있지 않을때를 추가해주었다.
                stack.pop()
            else:
                print('NO')
                break

    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
