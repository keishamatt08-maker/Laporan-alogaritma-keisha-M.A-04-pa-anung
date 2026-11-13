#Keisha Maulia Attahyah
#065002600004
#Laporan Praktikum Ke-5 Alogaritma dan Pemrograman

total_harga = 0.0
while True:
  masukan = input("masukkan umur: ")
  if not masukan.strip():
    break
  umur = int(masukan)
  if umur <= 2:
    harga = 0.0
    print("Gratis")
  elif 3 <= umur <= 12:
    harga = 14.0
    print(f"Harga ${harga:.2f}")
  elif umur >= 65:
    harga = 18.0
    print(f"Harga ${harga:.2f}")
  else:
    harga = 23.0
    print(f"Harga ${harga:.2f}")
  total_harga += harga
  print(f"Running total: {total_harga:.2f}")
if total_harga > 0:
  uang_bayar = float(input("masukkan jumlah uang: "))
  kembalian = uang_bayar - total_harga
  print(f"Running kembalian: {kembalian:.2f}")