h, m = map(int, input().split())
time = h*60 + m - 45
alarm = 0
h = time//60
m = time % 60

if (h < 0):
    h = 24 + h
    print(h, m)
else:
    print(h, m)
