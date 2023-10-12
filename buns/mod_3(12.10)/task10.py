#10
matrix = []
zero_matrix = []
k = int(input())

for i in range(k):
    dop_values = []
    the_shifter = []
    for j in range(k):
        dop_values.append(j + 1)
        the_shifter.append(0)
    matrix.append(dop_values)
    zero_matrix.append(the_shifter)

for i in matrix:
    print(i)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        zero_matrix[j][i] = matrix[i][j]

print()

for r in zero_matrix:
    print(r)