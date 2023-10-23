import numpy as np

def dekomposisi_spl(A, b):
    n = len(A)
    L = np.zeros((n, n))  # Matriks segitiga bawah untuk dekomposisi
    U = np.zeros((n, n))  # Matriks segitiga atas untuk dekomposisi
    y = np.zeros(n)       # Solusi sementara L*y = b
    x = np.zeros(n)       # Solusi akhir U*x = y

    for i in range(n):
        # Mengisi diagonal L dengan 1
        L[i][i] = 1
        
        # Menghitung matriks U dan L
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
                
        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]
            
        # Menghitung y dengan metode forward substitution
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # Menghitung x dengan metode backward substitution
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return y, x, L, U

# Input dan Output
A = np.array([[2, 1, -1], [3, 2, 1], [1, 1, 1]])
b = np.array([8, 14, 4])
y, x, L, U = dekomposisi_spl(A, b)  # Memanggil fungsi dekomposisi_spl
print("Nilai y (solusi L*y = b):", y)  # Menampilkan solusi y
print("Nilai x (solusi U*x = y):", x)  # Menampilkan solusi x
print("Matriks L (Lower Triangle):", L)  # Menampilkan matriks segitiga bawah
print("Matriks U (Upper Triangle):", U)  # Menampilkan matriks segitiga atas
