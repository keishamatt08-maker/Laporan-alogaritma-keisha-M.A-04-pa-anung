#Keisha Maulia Attahyah
#0650002600004
#prakatikum 5 algoritma dan pemograman
'''Latihan membuat fungsi untuk menentukan peringkat nilai huruf'''
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
        peringkat = 1.50
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
    print(f"rata - rata nya adalah: {rata_rata}")
else:
    print("Tidak ada nilai yang dimasukkan.")