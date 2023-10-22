def evk(a, n):
    if a == 0:
        return n
    return evk(n % a, a)

print(evk(168,165))