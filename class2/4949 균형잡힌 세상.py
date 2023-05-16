while True:
    a = input()
    stack = []
    if a == '.':
        break

    for i in a:
        # 시작점 괄호
        if i == '[' or i == '(':
            stack.append(i)
        # 닫는 괄호들 구분하기
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    # stack이 비어있으면 yes
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
