import math                       # mendeklarasikan mengimpor library math untuk digunakan

def f(x):                         # mendefinisikan sebuah fungsi dengan nama f(x)
    return math.exp(x) - x        # bagian dari fungsi untuk penghitungan, return digunakan untuk mengembalikan nilai sebagai hasil dari fungsi saaat digunakan atau dipanggil

def bagiDua(a, b, tolerGalat):          # mendefinisikan sebuah fungsi dengan nama bagiDua(a,b,tolerGalat)
    while (b - a) / 2> tolerGalat:      # melakukan pengulangan hingga (b-a)/2 lebih besar dari tolerGalat dan sebagai proses pencarian akar dengan metode bagi dua
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# penginputan
a = -1                                   # batas interval bawah
b = 1                                    # batas interval atas
tolerGalat = 1e-3                        # toleransi galat yang diperbolehkan
akar = bagiDua(a, b, tolerGalat)         # rumus pencarian akar
print(f"Akarnya adalah {akar:.3f}")      # mencetak hasil keluaran dengan mengambil hasil dari rumus pencarian akar di atas
