import timeit

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

start = timeit.timeit()
print(fibonacci(5))
end = timeit.timeit()
print(end - start)