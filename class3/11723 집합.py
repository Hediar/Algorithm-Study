import sys
input = sys.stdin.readline

m = int(input())
# 중복제거를 위해 set()을 사용하도록 한다.
S = set()


for _ in range(m):
    arr = input().split()
    a = arr[0]

    if (len(arr) == 1):
        if(a == 'all'):
            S = set([x for x in range(1, 21)])   
        else: # empty
            S = set()
    else:
        b = int(arr[1])
        if (a == 'add'):
            S.add(b)
        elif(a == 'remove'):
            if b in S:
                S.discard(b)
        elif(a == 'check'):
            if b in S:
                print(1)
            else:
                print(0)
        elif(a == 'toggle'):
            if b in S:
                S.discard(b)
            else:
                S.add(b)
