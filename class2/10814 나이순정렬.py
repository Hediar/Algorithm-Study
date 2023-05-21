n = int(input())
member = []
for i in range(n):
    age, name = map(str, input().split())
    member.append([int(age), i, name])
member.sort()

for i in member:
    print(i[0], i[2])
