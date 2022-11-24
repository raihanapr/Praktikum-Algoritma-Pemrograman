print("____")
print("INVOICE")
print("Raihan Car Wash")
print("Cileungsi, Bogor")

import datetime
x=datetime.datetime.now()
print(x)

print("____")
str(input("Nama Pelanggan : "))

str(input("Alamat : "))

str(input("Nomor Telepon : "))

str(input("Masukan Merk Kendaran : "))
#example : Toyota innova, Honda Jazz dll
Nomor1= str(input("Masukan Nomor Polisi : "))
#example : B ... FGE, F ... IW
print("____")
print("Cuci Mobil otomatis atau touchless")
print("Total : Rp 45.000")
print("____")
Tagihan= int(input("Tagihan: "))
Bayar= int(input("Uang yang dibayar: "))
Kembalian =Bayar-Tagihan
print("____")
print("Kembalian ", Kembalian)

print("Terimakasih")