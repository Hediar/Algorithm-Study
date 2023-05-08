a, b = map(int, input().split())

# 큰 수를 작은 수로 계속 나눠서 반복적으로 수행하여 0이 될 때 나누는 수가 최대 공약수이다.


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    result = (a*b)//gcd(a, b)
    return result


print(gcd(a, b))
print(lcm(a, b))
