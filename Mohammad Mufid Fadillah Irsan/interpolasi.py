def linear_interpolation(x1, y1, x2, y2, x):
    if x1 == x2:  # Memeriksa apakah x1 dan x2 sama
        raise ValueError("x1 dan x2 tidak boleh sama")  # Menimbulkan pengecualian jika x1 dan x2 sama
    
    # Menghitung nilai interpolasi linear
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return y  # Mengembalikan nilai hasil interpolasi

# Contoh penggunaan
x1, y1 = 1.0, 2.0  # Koordinat titik pertama (x1, y1)
x2, y2 = 3.0, 4.0  # Koordinat titik kedua (x2, y2)
x = 2.5  # Titik x di mana interpolasi akan dilakukan
result = linear_interpolation(x1, y1, x2, y2, x)  # Memanggil fungsi interpolasi linear
print(f"Interpolasi di x={x} adalah y={result}")  # Menampilkan hasil interpolasi

