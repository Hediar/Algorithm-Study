N = int(input())
word = []
result = []
for i in range(N):
    word.append(input())
result = list(set(word))
result.sort()
result.sort(key=len)


for i in result:
    print(i)
