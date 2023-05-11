import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())  # 층
    n = int(input())  # 호
    people = [i for i in range(1, n+1)]  # 1호부터 ~
    for i in range(k):  # k층 까지
        for j in range(1, n):  # 1호 ~ n호
            people[j] += people[j-1]
    print(people[-1])  # n호를 구해야 하니까 마지막에 있는 것을 출력한다.
