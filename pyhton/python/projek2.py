# fungsi garis 

def garis1():
    print("======================================")
    

def garis2():
    print("======================================")




# perpus kosong untuk menyimpan buku
buku = []

# fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis1()
        print("bukukosong blokkk")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print ("[{}]] {}".format (indeks,buku [indeks]))
            garis1()
 
 
 
# fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("inputan id buku : "))
    if indeks > len(buku):
        print("id salahh blokk")
        garis2()
    else:
        judul_baru = input("judul baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("buku berhasil dirubah")
        show_buku()
        garis1()
        
        
  
# fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)
    garis2()
    print("buku berhasil di tambah")
    garis1()
    
# fungsi delete buku
def delete_buku():
    show_buku()
    indeks = int(input("inputkan id buku : "))
    if indeks > len(buku):
        print("id salahh blokkk")
    else:
        buku.remove(buku[indeks])
        garis1()
        print("buku berhasil di hapus!")
        garis2()


# menu untuk tampilan perpustakaan
def show_menu():
    print("\n")
    print("---selamat datang di perpustakaan---")
    print("1. show buku")
    print("2. insert buku")
    print("3. edit buku")
    print("4. delete buku")
    print("5. keluar")
    
    menu = int(input("pilih menu : >"))
    
    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()               
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print("salahh blokkkk")
        

# tampilkan menu
if __name__ == "__main__":
    while True: 
        show_menu()

