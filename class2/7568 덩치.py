T = int(input())
people = []
rank = 1
for i in range(T):
    people.append(list(map(int, input().split())))

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
