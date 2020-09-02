def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]

    if len(A) == 2 and len(A[0]) == 2:
        val = float(A[0][0]) * float(A[1][1]) - float(A[1][0]) * float(A[0][1])
        return val

    for fc in indices:

        As = [row[:] for row in A]
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * float(A[0][fc]) * sub_det

    return total


def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("MATRIX NOT INVERTIBLE")
                return -1
        for j in range(i + 1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(a) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret


def print_matrix(M, rows, cols):
    mat = [[round(x, 3) + 0 for x in row] for row in M]
    for i in range(rows):
        for j in range(cols):
            print(mat[i][j], end=' ')
        print('')

while True:
    choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice:""")
    if choice == "1":  # addition matrix
        print("Enter size of first matrix:")
        row1, col1 = map(int, input().split())
        print("Enter first matrix:")
        matrix1 = [[j for j in input().split()] for i in range(row1)]
        print("Enter size of second matrix:")
        row2, col2 = map(int, input().split())
        if row1 == row2 and col1 == col2:
            print("Enter second matrix:")
            matrix2 = [[j for j in input().split()] for i in range(row2)]

            matrix3 = [[float(matrix1[i][j]) + float(matrix2[i][j]) for j in range(col2)] for i in range(row1)]
            for i in range(row1):
                print(*matrix3[i])
        else:
            print("The operation cannot be performed.")

    elif choice == "2":  # multiplication of matrix with constant
        print("Enter size of matrix:")
        [row, col] = [int(i) for i in input().split()]
        print("Enter matrix:")
        mat = [[int(j) for j in input().split()] for i in range(row)]
        print("Enter constant:")
        C = int(input())
        mul_mat = [[mat[i][j] * C for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                print(mul_mat[i][j], end=' ')
            print('')
    elif choice == "3":  # Matrix * matrix
        print("Enter size of first matrix:")
        row1, col1 = map(int, input().split())
        print("Enter first matrix:")
        matrix1 = [[float(j) for j in input().split()] for i in range(row1)]
        print("Enter size of second matrix:")
        row2, col2 = map(int, input().split())
        print("Enter second matrix:")
        matrix2 = [[float(j) for j in input().split()] for i in range(row2)]
        res = [[0 for x in range(col2)] for y in range(row1)]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    # resulted matrix
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
        for i in range(row1):
            print(*res[i])
    elif choice == "4":  # Transpose of matrix
        ch = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:""")
        if ch == "1":  # main diagonal
            print("Enter size of matrix:")
            row1, col1 = map(int, input().split())
            print("Enter  matrix:")
            matrix1 = [[j for j in input().split()] for i in range(row1)]
            mul_mat = [[matrix1[i][j] for j in range(col1)] for i in range(row1)]
            for i in range(row1):
                for j in range(col1):
                    print(mul_mat[j][i], end=' ')
                print('')
        elif ch == "2":  # side diagonal
            print("Enter size of matrix:")
            row, col = map(int, input().split())
            print("Enter matrix:")
            matrix = [[j for j in input().split()] for i in range(row)]
            mat = [[matrix[i][j] for j in range(col)] for i in range(row)]
            for j in reversed(range(col)):
                for i in reversed(range(row)):
                    print(mat[i][j], end=' ')
                print('')
        elif ch == "3":  # vertical matrix
            print("Enter size of matrix:")
            row, col = map(int, input().split())
            print("Enter matrix:")
            matrix = [[j for j in input().split()] for i in range(row)]
            mat = [[matrix[i][j] for j in range(col)] for i in range(row)]
            for j in range(col):
                for i in reversed(range(row)):
                    print(mat[j][i], end=' ')
                print('')
        elif ch == "4":  # horizontal matrix
            print("Enter size of matrix:")
            row, col = map(int, input().split())
            print("Enter matrix:")
            matrix = [[j for j in input().split()] for i in range(row)]
            mat = [[matrix[i][j] for j in range(col)] for i in range(row)]
            for j in reversed(range(col)):
                for i in range(row):
                    print(mat[j][i], end=' ')
                print('')
    elif choice == "5":  # Determinant of matrix
        print("Enter matrix size:")
        row, col = map(int, input().split())
        print("Enter matrix:")
        matrix = [[j for j in input().split()] for i in range(row)]
        print(determinant_recursive(matrix))
    elif choice == "6":
        print("Enter matrix size:")
        roww, coll = map(int, input().split())
        print("Enter matrix:")
        matrix = [[float(j) for j in input().split()] for i in range(roww)]
        if determinant_recursive(matrix) == 0:
            print("This matrix doesn't have an inverse")
        else:
            print_matrix(inverse(matrix), roww, coll)

    elif choice != "1" or "2" or "3" or "4" or "5" or "6":
        exit()
