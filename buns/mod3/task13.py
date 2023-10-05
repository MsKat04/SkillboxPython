s = input()
ko=''
kl=''
for i in range(1,len(s), 2):
    ko += s[i]+' '
for k in range(0,len(s),2):
    kl += s[k] + ' '

#print(ko ,kl)
sum_even=0
sum_odd=0
for i in range(0,len(ko)):
    if ko[i] != ' ':
        f = ko[i]
        sum_even += int(f)
for k in range(0,len(kl)):
    if kl[k] != ' ':
        d = kl[k]
        sum_odd += int(d)
#print(sum_even, sum_odd)
if ((3*sum_even) +  sum_odd) % 10 == 0:
    print("yeees")
else:
    print("nooo")