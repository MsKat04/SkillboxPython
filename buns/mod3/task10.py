a = input()
k = ''
d = ''
while len(a) > 0:
        if a[0] != ' ':
            k += a[0]
            a = a[1:]
        else:
            d += (k[-1])
            a = a[1:]
            k = ''
f = (k[-1])
print(d + f)
