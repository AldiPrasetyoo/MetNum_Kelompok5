def substitusi_maju(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

def substitusi_mundur(matrix, b):
    n = len(matrix)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

def eliminasi_gauss(matrix, b):
    segitiga_atas = True

    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                segitiga_atas = False
                break

    if segitiga_atas:
        x = substitusi_mundur(matrix, b)
    else:
        x = substitusi_maju(matrix, b)

    return x

# Meminta ukuran matriks A
n = int(input("Masukkan ukuran matriks A: "))

# Memasukkan matriks A
A = []
print("Masukkan matriks A:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Memasukkan vektor b
b = list(map(float, input("Masukkan vektor b: ").split()))

# Menghitung solusi
solusi = eliminasi_gauss(A, b)

# Menampilkan hasil
print("Solusi sistem persamaan linear:")
for i, x in enumerate(solusi):
    print(f'x{i+1} = {x}')
