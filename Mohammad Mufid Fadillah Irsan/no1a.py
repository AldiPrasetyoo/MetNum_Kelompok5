import numpy as np  # Mengimpor library numpy untuk digunakan

def f(x):  # Mendefinisikan sebuah fungsi dengan nama f(x)
    return x**3 - 2*x + 1  # Bagian dari fungsi untuk penghitungan, 'return' digunakan untuk mengembalikan nilai sebagai hasil dari fungsi saat digunakan atau dipanggil

def bagiDua(f, a, b, tolerGalat):  # Mendefinisikan sebuah fungsi dengan nama 'bagiDua' dengan parameter (f, a, b, tolerGalat)
    if np.sign(f(a)) == np.sign(f(b)):  # Memeriksa kondisi fungsi a dan b dengan np.sign yang berfungsi sebagai pengambil tanda dari fungsi tersebut.
        raise Exception('Tidak ada akar pada interval a dan b')  # Ketika tanda negatif dari kedua fungsi tersebut sama, maka akan muncul pesan "Tidak ada akar" karena dalam akar tidak boleh memiliki tanda yang sama.
    while (b - a) / 2 > tolerGalat:  # Melakukan pengulangan hingga (b-a)/2 lebih besar dari tolerGalat sebagai proses pencarian akar dengan metode bagi dua.
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return (a + b) / 2

# Penginputan
a = -2  # Batas interval bawah
b = 2  # Batas interval atas
tolerGalat = 1e-3  # Toleransi galat yang diperbolehkan
akar = bagiDua(f, a, b, tolerGalat)  # Rumus pencarian akar
print(f"Akarnya adalah {akar:.3f}")  # Mencetak hasil keluaran dengan mengambil hasil dari rumus pencarian akar di atas dengan hasil 3 angka di belakang koma.
