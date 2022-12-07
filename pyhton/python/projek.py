
def garis():
    print("-----------------------------------------------------------")


# SELAMAT DATANG DI JP HOTEL.
print("Selamat Datang DI JPHOTEL, Silahkan Pilih--")
print("--No-----TIPE----------HARGA--")
print("--01-----Suite-----1.000.000--")
print("--02-----Royal-------500.000--")

print("--03-----BPJS--------250.000--")

# Sampe Resepsionis (input data)
garis()
cust = input("Masukan Nama Lengkap : ")
tipe = int(input("Tipe : "))
lama_inap = int(input("Masukan Lama Menginap : "))
    
# tipe kamar
if tipe == 1:
     tipe_kamar = ("suite")
elif tipe == 2:
    tipe_kamar = ("Royal")
elif tipe == 3:
    tipe_kamar = ("BPJS")
    
# kalkulasi harga total
if tipe == 1:
    total_harga = 1000000*lama_inap
elif tipe == 2:
    total_harga = 500000*lama_inap
elif tipe == 3:
    total_harga = 250000*lama_inap

    
# struk JPHOTEL

print ("Terimakasih Atas Nama : ", cust)
print ("Tipe kamar yang Dipilih : ", tipe_kamar)
print ("Lama Menginap : ", lama_inap)
print ("total : ","Rp", total_harga,",00" )
garis()
