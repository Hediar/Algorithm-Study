import sys
n = int(sys.stdin.readline())


def factorial(n):
    if (n > 1):
        return n * factorial(n - 1)
    else:
        return 1


num = str(factorial(n))
cnt = 0
if len(num) == 1:  # 길이가 1일 경우
    print(0)
else:
    for i in num[::-1]:  # 뒤집어주기
        if i != '0':  # 0 이 아니라면
            break
        else:
            cnt += 1
    print(cnt)
