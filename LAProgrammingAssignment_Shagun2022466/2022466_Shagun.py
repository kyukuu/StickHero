file = open("matrices.txt", "r+")
matrix = [list(map(float, i.split())) for i in file]


def swapRows(matrix, a, b):
    matrix[a], matrix[b] = matrix[b], matrix[a]


def normalise(matrix, i, r, l):
    matrix[i] = [iVal - matrix[i][l]*rVal for rVal,
                 iVal in zip(matrix[r], matrix[i])]


def makelOne(matrix, i, l):
    matrix[i] = [matIValue / float(matrix[i][l]) for matIValue in matrix[i]]


def RREF(Matrix_initial):
    if not Matrix_initial:
        return Matrix_initial
    rows = len(Matrix_initial)
    columns = len(Matrix_initial[0])
    l = 0
    for r in range(rows):
        i = r
        if columns <= l:
            return Matrix_initial
        while Matrix_initial[i][l] == 0:
            i += 1
            if i == rows:
                l += 1
                if columns == l:
                    return Matrix_initial
                i = r
        swapRows(Matrix_initial, i, r)
        makelOne(Matrix_initial, r, l)
        for i in range(rows):
            if i != r:
                normalise(matrix, i, r, l)
        l += 1
    return Matrix_initial


answer = (RREF(matrix))
pivot = []
print("The RREF of the matrix is: ")
for i in answer:
    print(str(i))


def parm(answer):
    rows = len(answer)
    cols = len(answer[0])
    return rows, cols


rows, cols = parm(matrix)

column_indexes = []
for i in range(len(matrix[0])):
    column_indexes.append(i)


def pivot(answer):
    pivots = []
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j] != 0:
                pivots.append(j)
                break
    return pivots
pivots=pivot(answer)

def nonpivot(answer):
    non_pivots = []
    for i in column_indexes:
        if i not in pivots:
            non_pivots.append(i)
    return non_pivots
non_pivots=nonpivot(answer)


transpose = list(zip(*answer))
vect = []
for i in non_pivots:
    temp = [0]*cols
    for j in range(cols):
        if j == i:
            temp[j] = 1

    for j in range(cols):
        if j == i:
            for k in range(rows):
                if transpose[j][k] != 0:
                    temp[pivots[k]] = -transpose[j][k]
    vect.append(temp)


if len(vect) == 0:
    print("Only trivial solution exists")
else:
    print("Solution: ")
    for i in range(len(vect)):
        if i != len(vect)-1:
            print(f'x{non_pivots[i]+1}{vect[i]}', end=" + ")
            print()
        else:
            print(f'x{non_pivots[i]+1}{vect[i]}')

