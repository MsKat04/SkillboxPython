i = input()
n = int(input())
k='abcdefghijklmnopqrstuvwxyz'
kol = ''
if i in k:
    offset = ord(i) - ord('a') + n
    kol = chr(ord('a') + (offset % len(k)))
print(kol)
