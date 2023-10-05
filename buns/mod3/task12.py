
s = input()
k=''
for i in range(0, len(s)):
        if s[i] != '(' and s[i] !=')' and s[i] != ' ' and s[i] != '-':
           k +=s[i]
print(k)