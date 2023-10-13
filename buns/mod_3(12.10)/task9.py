def robot(n):
    x, y = 0, 0
    k = 0
    size = 1
    while k < n:

        for i in range(size):
            x -= 1
            y -= 1
            k += 1
            if k == n:
                return x, y
        size += 1

        for i in range(size):
            x += 1
            #y += 1
            k += 1
            if k == n:
                return x, y

        for i in range(size):
            k += 1
            y += 1
            if k == n:
                return x, y

        size += 1


n = int(input())
if n == 0:
    print("0, 0")
else:
    x, y = robot(n)
    print((x, y))