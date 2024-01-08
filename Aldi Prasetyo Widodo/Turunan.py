def hitung_turunan(fungsi, x, h, orde=1):
    if orde == 1:
        turunan_maju = (fungsi(x + h) - fungsi(x)) / h
        turunan_mundur = (fungsi(x) - fungsi(x - h)) / h
        turunan_pusat = (fungsi(x + h) - fungsi(x - h)) / (2 * h)
        
        return turunan_maju, turunan_mundur, turunan_pusat
    elif orde > 1:
        # Metode turunan orde tinggi (gunakan metode yang sesuai untuk orde yang diinginkan)
        # Contoh: turunan orde dua
        turunan_orde_dua = (fungsi(x + h) - 2 * fungsi(x) + fungsi(x - h)) / (h**2)
        return turunan_orde_dua
    else:
        print("Order turunan tidak valid.")

# mendefinisikan fungsi yang ingin kita turunkan
def f(x):
    return x**2

x0 = 4
h0 = 0.001

# Turunan orde pertama
turunan_maju, turunan_mundur, turunan_pusat = hitung_turunan(f, x0, h0, orde=1)
print("Turunan Maju:", turunan_maju)
print("Turunan Mundur:", turunan_mundur)
print("Turunan Pusat:", turunan_pusat)

# Turunan orde kedua
turunan_orde_dua = hitung_turunan(f, x0, h0, orde=2)
print("Turunan Orde Kedua:", turunan_orde_dua)
