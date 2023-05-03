N = int(input())
a = list(map(int, input().split()))

M = int(input())
arr = list(map(int, input().split()))

# 중복원소 제거
a_set = set(a)

# arr 리스트를 순회하면서 수의 존재 여부를 판단한다.
for i in arr:
    if i in a_set:
        print(1)
    else:
        print(0)
