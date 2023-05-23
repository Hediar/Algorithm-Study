import sys
n = int(sys.stdin.readline())
# push 명령일 경우 -> 출력 x, 입력만 하기
# pop 명령일 경우 -> 맨 위 정수 빼고 출력, 없으면 -1 출력
# size 명령일 경우-> 들어있는 정수의 개수
# empty 명령일 경우 -> 비어있으면 1, 아니면 0 출력
# top 명령일 경우 -> 가장 위에 있는 정수 출력, 없으면 -1 출력


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        if self.stack:
            x = self.stack[-1]
            self.stack.pop()
            print(x)
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if self.stack:  # 비어있지 않으면
            print(0)
        else:
            print(1)

    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)


myStack = Stack()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        myStack.push(int(command[1]))
    if command[0] == 'pop':
        myStack.pop()
    if command[0] == 'size':
        myStack.size()
    if command[0] == 'empty':
        myStack.empty()
    if command[0] == 'top':
        myStack.top()
