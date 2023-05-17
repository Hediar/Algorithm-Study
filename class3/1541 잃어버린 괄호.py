num = input().split('-')

result = 0
# if len(num) == 1:  # +만 있는 경우
#     for i in num[0].split('+'):
#         result += int(i)
#     print(result)
# else:
for i in num[0].split('+'):  # 배열의 첫번째는 더하기만 있다.
    result += int(i)

for i in num[1:]:  # 뒷 부분은 다 빼주면 된다.
    for j in i.split('+'):
        result -= int(j)
print(result)
