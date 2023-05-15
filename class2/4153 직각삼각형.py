import sys

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    list = [a,b,c]
    list.sort() 
    
    if (list[2]**2 == (list[0]**2 + list[1]**2)):
        print('right')
    else:
        print('wrong')
