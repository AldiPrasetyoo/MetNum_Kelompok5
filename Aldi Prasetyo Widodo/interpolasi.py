def linear_interpolation(x1, y1, x2, y2, x):
    if x1 == x2:        #Mengecek x1 dan x2 apakah sama atau tidak
        raise ValueError("x1 dan x2 tidak boleh sama")
    
    # Menghitung nilai interpolasi linear
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return y

# Contoh penggunaan
x1, y1 = 1.0, 2.0
x2, y2 = 3.0, 4.0
x = 2.5
result = linear_interpolation(x1, y1, x2, y2, x)
print(f"Interpolasi di x={x} adalah y={result}")
