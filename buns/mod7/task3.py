import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {func.__name__}: {end - start} секунд")
        return res
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper

# Функция fib без декораторов
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Применение декораторов к функции fib
memoized_fib = memoize(fib)
timed_med_fib = timer(memoized_fib)
timed_fib = timer(fib)

n = 30

print("Без декораторов:")
timed_fib(n)

print("\nС декоратором memoize:")
timed_med_fib(n)