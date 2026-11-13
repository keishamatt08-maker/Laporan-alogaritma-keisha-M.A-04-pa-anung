#Keisha Maulia Attahyah
#0650002600004
#prakatikum 6 algoritma dan pemograman


#Latihan Pertama

def ord_nilai_huruf(huruf):
    huruf
    if huruf == "A":
        peringkat = 4.00
    elif huruf == "A-":
        peringkat = 3.75
    elif huruf == "B+":
        peringkat = 3.50
    elif huruf == "B":
        peringkat = 3.00
    elif huruf == "B-":
        peringkat = 2.75
    elif huruf == "C+":
        peringkat = 2.50
    elif huruf == "C":
        peringkat = 2.00
    elif huruf == "C-":
        peringkat = 1.75
    elif huruf == "D":
        peringkat = 1.75
    elif huruf == "E":
        peringkat = 1.25
    else:
        peringkat = None    
    return peringkat
total_nilai = 0
jumlah_data = 0
while True:
    input_huruf = input("masukkan nilai: ").strip().upper()
    if input_huruf == "":
        break
    nilai = ord_nilai_huruf(input_huruf)
    if nilai is not None:
        if nilai.is_integer():
            print(f"nilai = {int(nilai)}")
        else:
            print(f"nilai = {nilai}")
        total_nilai += nilai
        jumlah_data += 1
    else:
        print("Nilai tidak sah!")
if jumlah_data > 0:
    rata_rata = total_nilai / jumlah_data
    print(f"rata - rata nya adalah:  {rata_rata}")
else:
    print("Tidak ada nilai yang dimasukkan.")
#latihan ke dua

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
