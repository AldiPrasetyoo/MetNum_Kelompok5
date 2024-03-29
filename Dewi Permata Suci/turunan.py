# -*- coding: utf-8 -*-
"""Turunan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLETM0gRSD8qxmVqo4Gpp_mpgA7sBfX2
"""

def turunan_maju(f, x, h):
    return (f(x + h) - f(x)) / h

while True:
    # Memasukkan persamaan fungsinya
    persamaan = input("\nMasukkan persamaan f(x) (gunakan x sebagai variabel): ")

    try:
        # Evaluasi ekspresi matematika
        fungsi = lambda x: eval(persamaan)

        # Memasukkan nilai x
        nilai_x = float(input(" nilai x: "))

        # Memasukkan nilai h
        nilai_h = float(input("nilai h: "))

        # Menggunakan metode turunan maju
        turunan_perkiraan = turunan_maju(fungsi, nilai_x, nilai_h)

        print(f"\nPerkiraan turunan pada x = {nilai_x} dengan h = {nilai_h} adalah {turunan_perkiraan}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")