def metode_simpson(fungsi, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    
    integral = 0
    
    for i in range(n):
        integral += (h / 6) * (fungsi(x[i]) + 4 * fungsi((x[i] + x[i+1]) / 2) + fungsi(x[i+1]))
    
    return integral

def metode_trapesium(fungsi, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    
    integral = 0
    
    for i in range(1, n):
        integral += fungsi(x[i])
    
    integral += (fungsi(a) + fungsi(b)) / 2
    integral *= h
    
    return integral

# Contoh fungsi yang akan diintegralkan
def f(x):
    return x**2 + 2*x + 1  

a = 0
b = 2
n = 100

# Memanggil fungsi metode Simpson
hasil_integral_simpson = metode_simpson(f, a, b, n)
print("Hasil Integral (Metode Simpson):", hasil_integral_simpson)

# Memanggil fungsi metode trapesium
hasil_integral_trapesium = metode_trapesium(f, a, b, n)
print("Hasil Integral (Metode Trapesium):", hasil_integral_trapesium)
