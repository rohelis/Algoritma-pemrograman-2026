# Program untuk mengecek apakah suatu bilangan bulat adalah bilangan prima

def cek_prima(n):
    # Bilangan prima harus lebih besar dari 1
    if n <= 1:
        return "Bukan Prima"
    
    # Periksa pembagi dari 2 sampai akar kuadrat n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Bukan Prima"
    
    return "Prima"

# -----------------------------
# Bagian utama program
# -----------------------------
if __name__ == "__main__":
    # Input dari pengguna
    n = int(input("Masukkan bilangan bulat: "))
    
    # Output hasil
    print(f"{n} adalah {cek_prima(n)}")

    # Contoh test case tambahan
    print("7:", cek_prima(7))    # Hasil: Prima
    print("12:", cek_prima(12))  # Hasil: Bukan Prima
