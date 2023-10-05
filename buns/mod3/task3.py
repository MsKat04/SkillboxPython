abc = input()
nul_str = abc.find(" ")
nul_str2 = abc.find(" ", nul_str + 1)

a = int(abc[:nul_str])
b = int(abc[nul_str + 1:nul_str2])
c = int(abc[nul_str2 + 1:])

if (a > b):
    if (c > a): print(a)
    elif (c > b): print(c)
    else:print(b)
elif(c > b):print(b)
elif (a > c):print(a)
else:print(c)

