# 3 objek, orang , pelajar, pekerja
# orang = kelas induk
# pelajar, pekerja = kelas turunan


class orang:
    def __init__(self, nama, kota):
        self.nama = nama
        self.kota = kota
        print("fungsi init dieksekusi")
        
    def perkenalan(self):
        print("halo nama saya",self.nama,"dari",self.kota)
        
class pelajar(orang):
    def __init__(self,nama,kota,sekolah):
        orang.__init__(self,nama,kota)
        self.sekolah = sekolah
    
class pekerja(orang):
    def __init__(self,nama,kota,kantor):
        super().__init__(nama,kota)
        self.kantor = kantor

        
eping = orang('eping','banteng\n')
eping.perkenalan()

anangis = pelajar('anangis','kolongjembatan','jp1\n')
anangis.perkenalan()
print(f'saya sekolah di{anangis.sekolah}\n')

pinn = pekerja('pinn','kutilanak','ptbongkarjaya')
pinn.perkenalan()
print(f'saya kerja di{pinn.kantor}\n')
