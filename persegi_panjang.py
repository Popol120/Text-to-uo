# Script Python Sederhana - Kalkulator Persegi Panjang
def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

def main():
    print("=== Kalkulator Persegi Panjang ===")
    
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        
        if panjang <= 0 or lebar <= 0:
            print("Error: Nilai harus positif")
            return
        
        luas = hitung_luas(panjang, lebar)
        keliling = hitung_keliling(panjang, lebar)
        
        print("\nHasil:")
        print("Luas:", luas)
        print("Keliling:", keliling)
        
    except ValueError:
        print("Error: Input harus angka")

if __name__ == "__main__":
    main()
