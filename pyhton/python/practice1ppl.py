#  praktek enkapsulasi



class siswa:
    def __init__(self, euroski):
        self.euroski = euroski
        

nama_siswa = siswa("eusroski")
print(f'1.siswa kami bernama {nama_siswa.euroski} ganteng') 


class guru:
    def __init__(self, anita):
        self._anita = anita
        
class nama (guru):
    def __init__(self, anita):
        super().__init__(anita)
        
    def panggil(self):
        print(f'2.guru kami bernama {self._anita} yang cantik')
        
       
susuk = nama('anita')
susuk.panggil()




class kepsek:
    def __init__(self, kepsek):
        self.__kepsek = kepsek
        
    def panggill(self):
        print(f'3.kepsek kami bernama {self.__kepsek} ')
        
        
        
nama_kepsek = kepsek('pak lilik')
nama_kepsek.panggill()    
        
        
    
               
    