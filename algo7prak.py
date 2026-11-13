#Keisha Maulia Attahyah
#065002600004
#Praktikum modul 7 algoritma dan pemograman
#latihan 1

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
def cetak_hasil():
  sandi = input("Masukkan angka : ")
  if sandi.lower() == "keluar":
    return False
  angka = int(sandi)
  if is_prime(angka):
    print(f"{angka} adalah bilangan Prima")
  else:
    print(f"{angka} bukanlah bilangan Prima")
  return True
while True:
  lanjut = cetak_hasil()
  if not lanjut:
    print("Program selesai.")
    break
  print("-" * 25)

#Keisha Maulia Attahyah
#065002600004
#Praktikum modul 7 algoritma dan pemograman
#latihan 2


def ordinal(n):
  if 11 <= n <= 13:
    sufiks = "th"
  else:
    sufiks = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
  return (n, sufiks)


print("Ordinal Number")
print("ketik 0 untuk mengentikan program")

while True:
  angka = int(input("masukkan angka: "))
  hasil = ordinal(angka)
  print(hasil)

  if angka == 0:
    print("terima kasih telah menggunakan program saya")
    break