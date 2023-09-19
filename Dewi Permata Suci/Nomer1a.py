import numpy as np # pustaka numpy untuk komputasi numerik

def f(x): # deklarasi fungsi f(x) dengan parameter x
    return x**3 - 2*x + 1 # lalu mengembalikan hasil dari fungsi x**3 - 2*x + 1

def metode_bagidua(f, a, b, tolerGalat): # deklarasi fungsi bagi dua untuk mencari nilai fungsi 'f' dalam interval '(a,b)' dengan toleransi eror 'e' 
    if np.sign(f(a)) == np.sign(f(b)): # memeriksa jika tanda f(a) sama dengan f(b)
        raise Exception('Tidak ada akar pada interval a dan b') # maka tidak ada akar dalam interval a dan b, dan kode akan memunculkan pengecualian (exception)
    
    while (b - a) / 2 > tolerGalat: # melakukan looping dengan kondisi sampai lebar interval [b - a] lebih kecil dari tolerGalat.
        m = (a + b) / 2 # mencari titik tengah interval (a,b)
        if f(m) == 0: # jika f(m)=0 maka f(m) adalah akar dari fungsi f
            return m # program akan mengembalikan nilai m
        elif np.sign(f(m)) == np.sign(f(a)): # jika tanda f(m) = tanda f(a) maka akar berada dalam interval (m,b)
            a = m # nilai a berubah menjadi nilai m
        else: # jika tanda f(m) != tanda f(a) maka akar berada dalam interval (a,m)
            b = m # nilai b berubah menjadi nilai m
    
    return (a + b) / 2 # mengembalikan nilai tengah dari interval (a,b) sebagai perkiraan akar dari fungsi f ketika loop selesai.

# Menggunakan metode Bagi Dua untuk mencari akar f(x)
a = -2  # Batas bawah interval
b = 2   # Batas atas interval
tolerGalat = 1e-3  # Tingkat toleransi error
akar = metode_bagidua(f, a, b, tolerGalat) # memangil fungsi metode_bagi dua kemudian di simpan di variabel akar
print(f"Akarnya adalah {akar:.3f}") # mencetak hasil dari akar dengan 3 angka di belakang koma