#membuat public class

class program_rpl1 :
    def __init__(self, kepala):
        self.kepala = kepala #public class declaration

#instansiasi
program_rpl = program_rpl1('kepala program rpl 1')

#print
print('ini adalah public class')
print(f'pak firman adalah {program_rpl.kepala}\n')


# membuat class protected
class rpl: #class induk
    def __init__(self, nama):
        self._nama = nama #protected class declaration

class gururpl(rpl): #class turunan
    def __init__(self, nama):
        super().__init__(nama) #panggil merk bagian sini

    def pamer(self):
        #hak akses _merk dari subclass
        print (f'pak arya adalah guru {self._nama}\n')

#instansiasi
print('ini adalah protected class')
rpl = gururpl('rpl')
rpl.pamer()


#membuat private class
class perpustakaan:
    def __init__(self, petugas):
        self.__petugas = petugas #private class declaration

    def tampilkan_perpustakaan(self):
        print(f'pak riyan adalah petugas {self.__petugas}')
        #panggil private disini

#intansiasi
print('ini adalah private class')
petugas = perpustakaan('perpustakaan')
petugas.tampilkan_perpustakaan()