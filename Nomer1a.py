import numpy as np          # mendeklarasikan mengimpor library numpy untuk digunakan

def f(x):                   # mendefinisikan sebuah fungsi dengan nama f(x)
    return x**3 - 2*x + 1   # bagian dari fungsi untuk penghitungan, return digunakan untuk mengembalikan nilai sebagai hasil dari fungsi saaat digunakan atau dipanggil

def bagiDua(f, a, b, tolerGalat):                                   # mendefinisikan sebuah fungsi dengan nama bagiDua(f,a,b,tolerGalat)
    if np.sign(f(a)) == np.sign(f(b)):                              # pengecekan kondisi fungsi a dan b dengan np.sigm berfunsi sebagai pengambil tanda dari fungsi tersebut, 
        raise Exception('Tidak ada akar pada interval a dan b')     # ketika tanda minus atau negatif dari kedua fungsi tersebut sama maka akan muncul "tidak ada akar" karena dalam akar tidak boleh memiliki tanda yg sama
    while (b - a) / 2 > tolerGalat:                                 # melakukan pengulangan hingga (b-a)/2 lebih besar dari tolerGalat dan sebagai proses pencarian akar dengan metode bagi dua
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return (a + b) / 2

        # penginputan
a = -2                                   # batas interval bawah
b = 2                                    # batas interval atas
tolerGalat = 1e-3                        # toleransi galat yang diperbolehkan
akar = bagiDua(f, a, b, tolerGalat)      # rumus pencarian akar
print(f"Akarnya adalah {akar:.3f}")      # mencetak hasil keluaran dengan mengambil hasil dari rumus pencarian akar di atas