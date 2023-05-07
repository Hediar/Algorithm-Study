n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))  # 각 자릿수를 더한다.
    d_sum = i + num  # 해당 숫자 + 각 자릿수의 합

    if d_sum == n:
        print(i)
        break
    elif i == n:  # 생성자가 없는 경우
        print(0)
