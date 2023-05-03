a = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in abc:
    if i in a:
        print(a.index(i), end=' ')
    else:
        print(-1, end=' ')
