class cal() :
    def __init__(self,a,b) :
       self.a = a
       self.b = b
    def tambah(self) :
        return self.a / self.b
    def kurang(self) :
        return self.a - self.b
        
a = int(input("Masukan Angka Pertama = "))
b = int(input("Masukan Angka Kedua = "))
obj = cal(a,b)
while True:
        def menu() :
        x = ('1. tambah \n2. kurang')
        print(x)  
        menu()
        break
pilihan = int(input('silahkan pilihan'))
if pilihan == 1:
        print("hasilnya : ", obj.tambah())
elif pilihan == 2:
        print("hasilnya : ", obj.kurang())
        
        