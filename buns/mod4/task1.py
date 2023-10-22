s = input().split(' ')
def num(n):
        if len(set(n)) == 1:
            return 'Все числа равны'
        elif len(n) == len(set(n)):
            return 'Все числа разные'
        else:
            return 'Есть равные и неравные числа'

print(num(s))