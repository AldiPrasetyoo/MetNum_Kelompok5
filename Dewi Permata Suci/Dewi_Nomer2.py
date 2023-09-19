import numpy as np                          # deklarasi impor library numpy untuk perhitungan
import matplotlib.pyplot as plt             # deklasrasi impor library matplotlib untuk grafik
from sympy import Symbol, lambdify, solve   # deklarasi impor library sympy untuk simbol-simbol di komputer

def bagiDua(f, a, b, e, maksIterasi): # deklarasi fungsi bagiDua  
    iterasi = 0 # iterasi awal = 0                         
    akar = None  # akar awal = none (belum ditemukan)                         

    while iterasi < maksIterasi: # loop berjalan selama jumlah iterasi (iterasi) kurang dari jumlah maksimum iterasi yang diizinkan (maksIterasi).         
        c = (a + b) / 2 # menghitung titik tengah c dari interval [a, b] menggunakan metode Bagi Dua.
        fc = f(c) # menghitung nilai fungsi f(c) pada titik tengah c.

        if abs(fc) < e: # kondisi yang memeriksa apakah nilai absolut dari f(c) lebih kecil dari toleransi galat e
            akar = c # Jika ya, maka c dianggap sebagai akar, 
            break # pencarian akar di hentikan

        if f(a) * fc < 0: # memeriksa jika hasil perkalian negatif,berarti akar berada di antara a dan c
            b = c # nilai b berubah menjadi c
        else: # memeriksa jika hasil perkalian positif,berarti akar berada di antara c dan b
            a = c # nilai a berubah menjadi c

        iterasi += 1 # iterasi bertambah setiap loop di jalankan

    return akar # jika loop selesai maka program mengeluarkan nilai akar

def plot_function(f, a, b, akar):   
    x = np.linspace(a, b, 1000) # membuat array x. menentukan titik pada sumbu x yang berada di antara nilai a dan b     
    y = [f(xi) for xi in x] # membuat array y dengan menggunakan fungsi f(xi) untuk setiap nilai xi dalam array x.

    # pembuatan gambar grafik
    plt.plot(x, y, label='f(x)') # menggambar grafik sesuai dengan array x pada sumbu x dan array y pada sumbu y. label f untuk memberi label pada garis
    if akar is not None: # memeriksa apakah akar tidak bernilai None. Jika akar ditemukan (tidak None), maka langkah berikutnya akan dijalankan                                      
        plt.scatter(akar, f(akar), color='red', label='Akar') # baris ini menambahkan titik merah pada grafik untuk menunjukkan lokasi akar. Koordinat titik adalah (akar, f(akar)), dengan warna merah (color='red'), dan label 'Akar'. 

    plt.axhline(0, color='black', linestyle='--', linewidth=0.7) # baris yang menggambar garis horizontal berwarna hitam pada y = 0 dalam grafik. Garis ini digunakan untuk menunjukkan sumbu x.
    plt.axvline(0, color='black', linestyle='--', linewidth=0.7) #  baris yang menggambar garis vertikal berwarna hitam pada x = 0 dalam grafik. Garis ini digunakan untuk menunjukkan sumbu y.

    # pengaturan grafik
    plt.xlabel('x') # pemberian label pada sumbu x dengan label x
    plt.ylabel('f(x)') # pemberian label pada sumbu y dengan label F(x)
    plt.title('Grafik Fungsi') # pemberian nama judul
    plt.legend() # penjelasan elemen yang ada dalam grafik
    plt.grid() # menambahkan garis pada grafik
    plt.show() # memberikan output atau melihatkan grafik yang sudah ada ditandai akar

# input data
x = Symbol('x')
fungsi_str = input("Masukkan fungsi : ")
fungsi = lambdify(x, fungsi_str, 'numpy')
a = float(input("Masukkan interval awal (a): "))
b = float(input("Masukkan interval akhir (b): "))
e = float(input("Masukkan Toleransi Galat (e): "))
n = int(input("Masukkan maksimum iterasi: "))

akar = bagiDua(fungsi, a, b, e, n) # memanggil fungsi bagi dua kemudian di simpan di variabel akar
if akar is not None:# memeriksa kondisi apabila akar tidak kosong 'None' 
    print(f'Akar persamaan: {akar:.3f}') # maka akan mencetak hasil akar dengan ketentukan 3 angka di belakang koma 
else:# pengecekan kondisi apabila akar kosong 'None' 
    print('Akar Tak Hingga.') # akan mencetak akar tak hingga

plot_function(fungsi, a, b, akar) #menampilkan grafik yang sudah dibentuk