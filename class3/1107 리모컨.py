n = int(input())  # target
m = int(input())  # 고장난 거 횟수
remote = {str(x) for x in range(10)}  # 0~9 문자열 set 객체 생성

if m != 0:
    remote -= set(input().split())  # 고장난 것 빼내기

ans = abs(100 - n)

for k in range(1000000):
    num = str(k)
    for i in range(len(num)):
        if num[i] not in remote:  # 0~999999까지의 숫자 순회하면서 리모컨 버튼에 없으면 넘긴다.
            break
        if i == len(num)-1:  # 마지막 자리수까지 확인다면 갱신해준다.
            ans = min(ans, abs(n-k)+len(num))

print(ans)
