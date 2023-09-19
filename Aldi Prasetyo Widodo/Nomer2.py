import numpy as np                          # deklarasi impor library numpy untuk perhitungan
import matplotlib.pyplot as plt             # deklasrasi impor library matplotlib untuk grafik
from sympy import Symbol, lambdify, solve   # deklarasi impor library sympy untuk simbol-simbol di komputer

def bagiDua(f, a, b, e, maksIterasi):     # mendefinisikan fungsi metode dengan nama bagi dua dengan parameter(f,a,b,e,maksIterasi)
    iterasi = 0                           # mendefinisikan iterasi pada saat ini masih 0
    akar = None                           # mendefinisikan akar pada saat ini belum ada atau none

    while iterasi < maksIterasi:          # melakukan pengulangan hingga iterasi sampai pada yg diinginkan dan sebagai proses pencarian akar dengan metode bagi dua
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

def plot_function(f, a, b, akar):   # mendefinisikan fungsi plot dengan parameter (f,a,b,akar). akar ini digunakan sebagai batas maksimum sumbu pada grafik
        # proses untuk pembuatan grafik x dan y
    x = np.linspace(a, b, 1000)     
    y = [f(xi) for xi in x]

        # pembuatan gambar grafik
    plt.plot(x, y, label='f(x)')
    if akar is not None:                                        #kondisi untuk memeriksa apakah akar ada atau tidak
        plt.scatter(akar, f(akar), color='red', label='Akar')   # jika ditemukan ada akar maka akan memberi titik pada grafik untuk memberi tahu ada akar

    plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.7)

        # pengaturan grafik
    plt.xlabel('x')               # pemberian label pada sumbu x dengan label x
    plt.ylabel('f(x)')            # pemberian label pada sumbu y dengan label F(x)
    plt.title('Grafik Fungsi')    # pemberian nama judul
    plt.legend()                  # penjelasan elemen yang ada dalam grafik
    plt.grid()                    # menambahkan garis pada grafik
    plt.show()                    # memberikan output atau melihatkan grafik yang sudah ada ditandai akar

# Penginputan data
x = Symbol('x')
fungsi_str = input("Masukkan fungsi : ")
fungsi = lambdify(x, fungsi_str, 'numpy')
a = float(input("Masukkan interval awal (a): "))
b = float(input("Masukkan interval akhir (b): "))
e = float(input("Masukkan Toleransi Galat (e): "))
n = int(input("Masukkan maksimum iterasi: "))

akar = bagiDua(fungsi, a, b, e, n)          # rumus mencari akar dengan metode bagi dua
if akar is not None:                        # pengecekan kondisi apabila akar tidak kosong maka akan mencetak hasil akar dari rumus diatas dengan ketentukan hasil 3 angka di belakang koma 
    print(f'Akar persamaan: {akar:.3f}')
else:                                       # pengecekan kondisi apabila akar kosong akan mencetak akar tak hingga
    print('Akar Tak Hingga.')

plot_function(fungsi, a, b, akar)           #menampilkan grafik yang sudah dibentuk