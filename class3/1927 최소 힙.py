"""
입력: 연산개수, 연산정보 x 

출력: 가장 작은 값, 비어있을 경우 0 
"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
data = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not data:  # 비어있을 경우
            print(0)
        else:
            print(heapq.heappop(data))
    else:
        heapq.heappush(data, x)

"""
힙으로 구현했던 것
class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''
    # 현재 인덱스 왼*2 오*2+1 -> 
    def __init__(self) :
        self.data = [0] #0에는 무엇을 곱해도 0이라 더미 데이터로 

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)

        index = len(self.data) - 1 #현재 가지고 있는 것 중에서 마지막 번호 
        #마지막으로 삽입한 값이 루트노드가 되면 반복문 종료
        while index != 1 :
                if self.data[index//2] > self.data[index] : #부모와 자식을 변경해주어야 함
                    #인덱스를 2로 나누면 부모노드에 접근가능(완전이진트리 특성)
                    temp = self.data[index]
                    self.data[index] = self.data[index//2]
                    self.data[index//2] = temp

                    index = index // 2
                else: #<=인 상황 
                    break



    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''

        if len(self.data) == 1:
            return

        #루트노드와 마지막노드를 바꿔치기 하고 데이터에서 pop을 하여 값을 버림
        #마지막 노드를 루트 노드 자리로 이동한다.
        self.data[1] = self.data[-1]
        self.data.pop() #원래 있던 루트노드가 사라짐 

        index = 1

        while True :
            # 1. 아무 자식도 없는 경우
            if len(self.data) -1 < index * 2 : #index*2는 왼쪽 자식 -> 왼쪽 자식의 길이보다 크다면 지금 가지고 있는 리스트에 없다 
                break
            # 2. 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < index * 2 + 1: #index*2 + 1 => 오른쪽 자식의 인덱스
                priority = index * 2 #왼쪽, 오른쪽 어디로 갈지 결정해주는 변수 
            #왼,오 모두 자식이 있는 경우
            else :
                if self.data[index*2] < self.data[index*2 + 1] :
                    priority = index * 2 #왼쪽 자식으로 이동 
                else:
                    priority = index * 2 + 1 #오른쪽 자식으로 이동

            #현재 가리키고 있는(제거된 자리를 채우기위해 루트노드로 옮겨진 자료)가 priority보다 크다면 위에서 아래로 값을 변경해줘야 한다. 
            if self.data[index] > self.data[priority] :
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp

                index = priority
            else: #작지 않다면 자리를 바꿀 수 없음 => 자식이 부모보다 커야 최소힙을 성립시키기 위해 바꾸는 것인데 아니라면 이미 최소힙의 요건을 충족시키고 있다는 의미 
                break


    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''

        if len(self.data) == 1:
            return -1 # 더미 데이터만 있는 상태

        else :
            return self.data[1] #루트 노드 반환
"""
