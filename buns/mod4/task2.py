def degree(a, n):
    def even(n):
        if n % 2 == 0:
            return True
        return False
    if n == 0:
        return 1
    if even(n):
        res = degree(a, n/2)
        return res*res
    return a * degree(a, n-1)


print(degree(2, 4))