while True:
    n = input()
    stack = []
    re_num = ''
    if n == '0':
        break
    else:
        for i in n:
            stack.append(i)
        for _ in range(len(stack)):
            re_num += stack.pop()
        if re_num == n:
            print('yes')
        else:
            print('no')
