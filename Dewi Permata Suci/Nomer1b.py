import math #import library math agar "e" bisa terdeteksi sebagai nilai

# Mendefinisikan fungsi dari soal
def f(x): 
    return math.exp(x) - x 

# Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua atau bisection
def bisection(a, b, tolerGalat):
    # Proses mencari akar
    while (b - a) / 2 > tolerGalat: #melakukan looping dengan kondisi sampai lebar interval [b - a] lebih kecil dari tolerGalat.
        c = (a + b) / 2.0 # mencari titik tengah interval (a,b)
        if f(c) == 0.0: # jika f(c)=0 maka f(c) adalah akar dari fungsi f
            return c # program akan mengembalikan nilai c
        elif f(a) * f(c) < 0.0: # jika tanda f(a) * tanda f(c)<0 maka akar berada dalam interval (a,c)
            b = c # nilai b berubah menjadi nilai c
        else: # jika  f(a) * f(c) maka akar berada dalam interval (c,b)
            a = c # nilai a berubah menjadi nilai c
    return (a + b) / 2.0 # mengembalikan nilai tengah dari interval (a,b) sebagai perkiraan akar dari fungsi f ketika loop selesai.

# Mendefinisikan interval awal [a, b] dan TolerGalat
a = -1.0 # batas bawah
b = 1.0 # batas atas
tolerGalat = 1e-3 # tingkat toleransi error

# Memanggil fungsi bisection untuk mencari akar
akar = bisection(a, b, tolerGalat) # memangil fungsi bisection dua kemudian di simpan di variabel akar
print(f"Akar hampiran:{akar:.3f}") # mencetak hasil dari akar dengan 3 angka di belakang koma