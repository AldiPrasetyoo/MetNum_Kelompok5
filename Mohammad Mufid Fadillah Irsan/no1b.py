import math  # Mengimpor library math untuk digunakan

def f(x):  # Mendefinisikan fungsi dengan nama f(x)
    return math.exp(x) - x  # Bagian dari fungsi untuk perhitungan, 'return' digunakan untuk mengembalikan nilai sebagai hasil dari fungsi saat digunakan atau dipanggil

def bagiDua(a, b, tolerGalat):  # Mendefinisikan sebuah fungsi dengan nama 'bagiDua' dengan parameter (a, b, tolerGalat)
    while (b - a) / 2 > tolerGalat:  # Melakukan pengulangan hingga (b-a)/2 lebih besar dari tolerGalat sebagai proses pencarian akar dengan metode bagi dua
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# inputan
a = -1  # Batas interval bawah
b = 1   # Batas interval atas
tolerGalat = 1e-3  # Toleransi galat yang diperbolehkan
akar = bagiDua(a, b, tolerGalat)  # Rumus untuk pencarian akar
print(f"Akarnya adalah {akar:.3f}")  # Mencetak hasil keluaran dengan mengambil hasil dari rumus pencarian akar di atas dengan hasil 3 angka di belakang koma.
