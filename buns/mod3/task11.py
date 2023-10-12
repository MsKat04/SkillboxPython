s = input()
b = False
for i in range(0, len(s)):
    for k in range(0, len(s)):
        if i!=k:
            if s[i] == s[k] and s[i] != ' ':
                b=True
print(b)