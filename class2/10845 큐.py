import sys
n = int(sys.stdin.readline())
# push 명령일 경우 -> 입력
# pop 명령일 경우 -> 맨 앞의 정수 빼고 출력, 없으면 -1 출력
# size 명령일 경우-> 들어있는 정수의 개수
# empty 명령일 경우 -> 비어있으면 1, 아니면 0 출력
# front 명령일 경우 -> 가장 앞에 있는 정수 출력, 없으면 -1 출력
# back 명령일 경우 -> 가장 뒤에 있는 정수 출력, 없으면 -1 출력


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, a):
        self.queue.append(a)

    def pop(self):
        if self.queue:
            print(self.queue[0])
            del self.queue[0]
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

    def empty(self):
        if self.queue:  # 비어있지 않으면
            print(0)
        else:
            print(1)

    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)

    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)


myQueue = Queue()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        myQueue.push(int(command[1]))
    if command[0] == 'pop':
        myQueue.pop()
    if command[0] == 'size':
        myQueue.size()
    if command[0] == 'empty':
        myQueue.empty()
    if command[0] == 'front':
        myQueue.front()
    if command[0] == 'back':
        myQueue.back()
