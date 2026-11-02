def is_kabisat(tahun):
    return (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0)

def hitung_jumlah_hari(bulan, tahun):
    if bulan == 2:
        return 29 if is_kabisat(tahun) else 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31

print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))
    
    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break
        
    if bulan == 2:
        tahun = int(input("masukkan tahun (e.g., 2021): "))
        print(f"{hitung_jumlah_hari(bulan, tahun)} hari dalam sebulan")
    elif 1 <= bulan <= 12:
        print(f"{hitung_jumlah_hari(bulan, 0)} hari dalam sebulan")
    else:
        print("Bulan tidak valid, silakan coba lagi.")
