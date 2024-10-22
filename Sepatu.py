class Sepatu:
    def __init__(self, namaSepatu: str, merek: str, warna: str, ukuran: float, jenis: str, kondisi: str = "Baru"):
        self.namaSepatu = namaSepatu
        self.merek = merek
        self.warna = warna
        self.ukuran = ukuran
        self.jenis = jenis
        self.kondisi = kondisi
    
    def getMerek(self) -> str:
        return self.merek

    def setMerek(self, merek: str) -> None:
        self.merek = merek

    def getWarna(self) -> str:
        return self.warna

    def setWarna(self, warna: str) -> None:
        self.warna = warna

    def getUkuran(self) -> float:
        return self.ukuran

    def setUkuran(self, ukuran: float) -> None:
        self.ukuran = ukuran

    def getJenis(self) -> str:
        return self.jenis

    def setJenis(self, jenis: str) -> None:
        self.jenis = jenis

    def getKondisi(self) -> str:
        return self.kondisi

    def setKondisi(self, kondisi: str) -> None:
        self.kondisi = kondisi

    def isMuat(self, ukuranKaki: float) -> bool:
        return abs(self.ukuran - ukuranKaki) <= 0.5

    def detailSepatu(self) -> str:
        return (f"Nama Sepatu   : {self.namaSepatu}\n"
                f"Merek Sepatu  : {self.merek}\n"
                f"Warna Sepatu  : {self.warna}\n"
                f"Ukuran Sepatu : {self.ukuran}\n"
                f"Jenis Sepatu  : {self.jenis}\n"
                f"Kondisi Sepatu: {self.kondisi}")


