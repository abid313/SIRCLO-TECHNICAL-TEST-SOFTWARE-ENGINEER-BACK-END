from abc import ABC, abstractmethod

class kapal(ABC):
    
    @abstractmethod
    def __init__(self, nama, kapasitas, jumlah_penumpang):
        self.nama = nama
        self.kapasitas = kapasitas
        self.jumlah_penumpang = jumlah_penumpang
    
class perahu_motor(kapal):
    
    var_warna = 'merah'
    
    def __init__(self, nama, kapasitas, jumlah_penumpang):
        super().__init__(nama, kapasitas, jumlah_penumpang)
        self.kapasitas = kapasitas
        self.jumlah_penumpang = jumlah_penumpang
    
    def cetak_informasi(self):
        print("Nama:", self.nama)
        print("Warna:", self.var_warna)
        print("Kapasitas:", self.kapasitas)
        print("Jumlah Penumpang:", self.jumlah_penumpang)

class perahu_layar(kapal):
    
    var_warna = 'biru'
    
    def __init__(self, nama, kapasitas, jumlah_penumpang):
        super().__init__(nama, kapasitas, jumlah_penumpang)
        self.kapasitas = kapasitas
        self.jumlah_penumpang = jumlah_penumpang
    
    def cetak_informasi(self):
        print("Nama:", self.nama)
        print("Warna:", self.var_warna)
        print("Kapasitas:", self.kapasitas)
        print("Jumlah Penumpang:", self.jumlah_penumpang)
    
class pesiar(kapal):
    
    var_warna = 'kuning'
    
    def __init__(self, nama, kapasitas, jumlah_penumpang):
        super().__init__(nama, kapasitas, jumlah_penumpang)
        self.kapasitas = kapasitas
        self.jumlah_penumpang = jumlah_penumpang
    
    def cetak_informasi(self):
        print("Nama:", self.nama)
        print("Warna:", self.var_warna)
        print("Kapasitas:", self.kapasitas)
        print("Jumlah Penumpang:", self.jumlah_penumpang)

perahuMotor = perahu_motor("Perahu Motor", "2 orang", "1 orang")
perahuLayar = perahu_layar("Perahu Layar", "13 orang", "8 orang")
pesiar = pesiar("Pesiar", "3500 orang", "2139 orang")

perahuMotor.cetak_informasi()
print("----------------------------------------------------")
perahuLayar.cetak_informasi()
print("----------------------------------------------------")
pesiar.cetak_informasi()
