s = input()
rusg='бвгджзйклмнпрстфхцчшщ'
rusc='аеёиоуыэюя'
kc=0
kg = 0
while len(s) > 0:
        if s[0] != ' ' and s[0] in rusc:
            kc += 1
            s = s[1:]
        elif s[0] != ' ' and s[0] in rusg:
            kg+=1
            s = s[1:]
        else:
            s = s[1:]
print(kc, kg)