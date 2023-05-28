n, k = map(int, input().split())
# n! // (n-k)! * k!


def factorial(n):
    if (n > 1):
        return n * factorial(n-1)
    else:
        return 1


result = factorial(n) // (factorial(n-k) * factorial(k))
print(result)
