def linear_interpolation(x1, y1, x2, y2, x):
    # Mengecek agar x1 tidak sama dengan x2 (mencegah pembagian dengan nol)
    if x1 == x2:
        raise ValueError("x1 dan x2 tidak boleh sama")
    
    # Menghitung nilai interpolasi linear
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return y

# Meminta input dari pengguna
x1 = float(input("nilai x1: "))
y1 = float(input("nilai y1: "))
x2 = float(input("nilai x2: "))
y2 = float(input("nilai y2: "))
x = float(input("nilai x untuk interpolasi: "))

# Memanggil fungsi linear_interpolation dan mencetak hasilnya
try:
    result = linear_interpolation(x1, y1, x2, y2, x)
    print(f"Interpolasi di x={x} adalah y={result}")
except ValueError as e:
    print(e)
