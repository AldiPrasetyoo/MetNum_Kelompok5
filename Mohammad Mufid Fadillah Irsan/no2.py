import numpy as np                          # Import library numpy untuk perhitungan
import matplotlib.pyplot as plt             # Import library matplotlib untuk grafik
from sympy import Symbol, lambdify, solve   # Import library sympy untuk simbol-simbol di komputer

def bagiDua(f, a, b, e, maksIterasi):     # Mendefinisikan fungsi metode dengan nama "bagiDua" dengan parameter (f, a, b, e, maksIterasi)
    iterasi = 0                           # Mendefinisikan iterasi pada saat ini masih 0
    akar = None                           # Mendefinisikan akar pada saat ini belum ada atau "None"

    while iterasi < maksIterasi:          # Melakukan pengulangan hingga iterasi mencapai maksimum yang diinginkan, ini merupakan proses pencarian akar dengan metode bagi dua
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < e:
            akar = c
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iterasi += 1

    return akar

def plot_function(f, a, b, akar):   # Mendefinisikan fungsi "plot_function" dengan parameter (f, a, b, akar). Akar ini digunakan sebagai batas maksimum sumbu pada grafik.
    # Proses untuk pembuatan grafik x dan y
    x = np.linspace(a, b, 1000)
    y = [f(xi) for xi in x]

    # Pembuatan gambar grafik
    plt.plot(x, y, label='f(x)')
    if akar is not None:  # Kondisi untuk memeriksa apakah akar ada atau tidak
        plt.scatter(akar, f(akar), color='red', label='Akar')  # Jika ditemukan akar, maka akan memberi titik pada grafik untuk menunjukkan lokasi akar.

    plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.7)

    # Pengaturan grafik
    plt.xlabel('x')               # Label pada sumbu x
    plt.ylabel('f(x)')            # Label pada sumbu y
    plt.title('Grafik Fungsi')    # Nama judul grafik
    plt.legend()                  # Penjelasan elemen yang ada dalam grafik
    plt.grid()                    # Menambahkan garis pada grafik
    plt.show()                    # Menampilkan grafik yang sudah dibentuk

# Penginputan data
x = Symbol('x')
fungsi_str = input("Masukkan fungsi: ")    # Meminta pengguna untuk memasukkan fungsi
fungsi = lambdify(x, fungsi_str, 'numpy')
a = float(input("Masukkan interval awal (a): "))   # Meminta pengguna untuk memasukkan interval awal (a)
b = float(input("Masukkan interval akhir (b): "))  # Meminta pengguna untuk memasukkan interval akhir (b)
e = float(input("Masukkan Toleransi Galat (e): "))  # Meminta pengguna untuk memasukkan toleransi galat (e)
n = int(input("Masukkan maksimum iterasi: "))      # Meminta pengguna untuk memasukkan maksimum iterasi

akar = bagiDua(fungsi, a, b, e, n)          # Rumus mencari akar dengan metode bagi dua
if akar is not None:                        # Pengecekan kondisi: jika akar tidak kosong, maka cetak hasil akar dengan tiga angka di belakang koma
    print(f'Akar persamaan: {akar:.3f}')
else:                                       # Jika akar kosong, cetak pesan bahwa akar tak hingga
    print('Akar Tak Hingga.')

plot_function(fungsi, a, b, akar)           # Menampilkan grafik yang sudah dibentuk
