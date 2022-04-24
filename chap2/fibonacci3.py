import timeit

memo = {1: 1, 2: 1}
def fibonacci(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return memo[n]

start = timeit.timeit()
print(fibonacci(6))
end = timeit.timeit()
print(end - start)