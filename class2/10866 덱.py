import sys
n = int(sys.stdin.readline())
# push_front X -> 입력
# push_back X
# pop_front -> 맨 앞의 정수 빼고 출력, 없으면 -1 출력
# pop_back
# size 명령일 경우-> 들어있는 정수의 개수
# empty 명령일 경우 -> 비어있으면 1, 아니면 0 출력
# front 명령일 경우 -> 가장 앞에 있는 정수 출력, 없으면 -1 출력
# back 명령일 경우 -> 가장 뒤에 있는 정수 출력, 없으면 -1 출력


class DeQueue:
    def __init__(self):
        self.dequeue = []

    def push_back(self, a):
        self.dequeue.append(a)

    def push_front(self, a):
        self.dequeue

    def pop(self):
        if self.dequeue:
            print(self.dequeue[0])
            del self.dequeue[0]
        else:
            print(-1)

    def size(self):
        print(len(self.dequeue))

    def empty(self):
        if self.dequeue:  # 비어있지 않으면
            print(0)
        else:
            print(1)

    def front(self):
        if self.dequeue:
            print(self.dequeue[0])
        else:
            print(-1)

    def back(self):
        if self.dequeue:
            print(self.dequeue[-1])
        else:
            print(-1)


myDeQueue = DeQueue()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        myDeQueue.push(int(command[1]))

    if command[0] == 'pop':
        myDeQueue.pop()

    if command[0] == 'size':
        myDeQueue.size()
    if command[0] == 'empty':
        myDeQueue.empty()
    if command[0] == 'front':
        myDeQueue.front()
    if command[0] == 'back':
        myDeQueue.back()
