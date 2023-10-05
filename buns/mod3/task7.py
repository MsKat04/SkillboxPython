n = input()
k=0
l=0
for i in n:
    if i == '1':
        k += 1
    elif i == '0':
        l += 1

if k == l:
    print("yes")
else:
    print("no")