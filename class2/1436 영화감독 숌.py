n = int(input())
apo = 666
cnt = 0
while True:
    if '666' in str(apo):  # apo에 666이 있는지 확인
        cnt += 1  # 해당 숫자를 N번째로 정의
        if cnt == n:  # 내가 찾는 n값과 같으면 종료
            break
    apo += 1
print(apo)
