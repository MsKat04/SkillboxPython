a = input()
k = ''
while len(a) > 0:
        if a[0] != '.':
            k += a[0]
            a = a[1:]
        else:
            print(k)
            a = a[1:]
            k = ''
print(k)
