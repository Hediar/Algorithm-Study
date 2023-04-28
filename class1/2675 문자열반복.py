T = int(input())

for i in range(T):
    result = []
    r, s = input().split()
    r = int(r)
    for j in range(len(s)):
        result.append(s[j]*r)
    print(''.join(result))
