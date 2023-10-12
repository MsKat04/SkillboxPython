'''l_k = input().split(' ')
l_n = input().split(' ')
l_m = input().split(' ')
#if len(l_k) < 3:
#   print("jjjj")

m=[]
m.append(l_k)
m.append(l_n)
m.append(l_m)
print(m)
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == m[i][j]:
            print('f')

for i in range(len(l_k)):
    for j in range(len(l_n)):
        for k in range(len(l_m)):
            if l_k[i] == l_n[j] and l_n[j] == l_m[k]:
                print("f")'''


m1 = input().split(' ')
m2 = input().split(' ')
m3 = input().split(' ')
def game(matrix):
    k = len(m1)

    for row in matrix:
        if row.count('X') == k:
            return 'X'
        elif row.count('O') == k:
            return 'O'

    for col in range(k):
        if [matrix[row][col] for row in range(k)].count('X') == k:
            return 'X'
        elif [matrix[row][col] for row in range(k)].count('O') == k:
            return 'O'
    else:
        return'Ничья'

matrix=[]
matrix.append(m1)
matrix.append(m2)
matrix.append(m3)


print('RESULT:', game(matrix))