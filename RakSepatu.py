from Sepatu import Sepatu

class RakSepatu:
    def __init__(self, pemilik: str, ukuranKaki: float, slotSepatu: int, sepatu: list = []):
        self.pemilik = pemilik
        self.ukuranKaki = ukuranKaki
        self.slotSepatu = slotSepatu
        self.sepatu = sepatu

    def getPemilik(self) -> str:
        return self.pemilik

    def setPemilik(self, pemilik: str) -> None:
        self.pemilik = pemilik

    def getUkuranKaki(self) -> float:
        return self.ukuranKaki

    def setUkuranKaki(self, ukuranKaki: float) -> None:
        self.ukuranKaki = ukuranKaki

    def getSepatu(self) -> list:
        return self.sepatu

    def setSepatu(self, sepatu: list) -> None:
        self.sepatu = sepatu

    def getSlotSepatu(self) -> int:
        return self.slotSepatu

    def setSlotSepatu(self, slotSepatu: int) -> None:
        self.slotSepatu = slotSepatu

    def sisaSlotKosong(self) -> int:
        return self.slotSepatu - len(self.sepatu)

    def jualSepatu(self, namaSepatu: str) -> None:
        found = False
        for s in self.sepatu:
            if s.namaSepatu == namaSepatu:
                self.sepatu.remove(s)
                found = True
                print(f"Sepatu {namaSepatu} berhasil dijual.")
                break
        if not found:
            print(f"Sepatu {namaSepatu} tidak ditemukan.")

    def beliSepatu(self, namaSepatu: str, merek: str, warna: str, ukuran: float, jenis: str) -> None:
        if self.sisaSlotKosong() == 0:
            print("Rak sepatu penuh, sepatu gagal dibeli.")
            return
        for s in self.sepatu:
            if s.namaSepatu == namaSepatu:
                print(f"Sepatu dengan nama {namaSepatu} sudah ada, sepatu gagal dibeli.")
                return
        sepatuBaru = Sepatu(namaSepatu, merek, warna, ukuran, jenis)
        self.sepatu.append(sepatuBaru)
        print(f"Sepatu {namaSepatu} berhasil dibeli.")

    def pakaiSepatu(self, namaSepatu: str) -> None:
        for s in self.sepatu:
            if s.namaSepatu == namaSepatu:
                if s.isMuat(self.ukuranKaki):
                    s.setKondisi("Kotor")
                    print(f"Sepatu {namaSepatu} berhasil dipakai.")
                else:
                    print(f"Ukuran sepatu {namaSepatu} tidak pas, sepatu gagal dipakai.")
                return
        print(f"Sepatu {namaSepatu} tidak ditemukan.")

    def cuciSepatu(self, namaSepatu: str) -> None:
        for s in self.sepatu:
            if s.namaSepatu == namaSepatu:
                if s.getKondisi() == "Kotor":
                    s.setKondisi("Bersih")
                    print(f"Sepatu {namaSepatu} berhasil dicuci.")
                elif s.getKondisi() == "Bersih":
                    print(f"Sepatu {namaSepatu} sudah bersih, tidak perlu dicuci.")
                elif s.getKondisi() == "Baru":
                    print(f"Sepatu {namaSepatu} masih baru, tidak perlu dicuci.")
                return
        print(f"Sepatu {namaSepatu} tidak ditemukan.")

    def detailRak(self) -> None:
        print(f"== Rak Sepatu ==\n"
              f"Nama Pemilik      : {self.pemilik}\n"
              f"Ukuran Kaki Pemilik: {self.ukuranKaki}\n"
              f"Slot Sepatu       : {self.slotSepatu}\n"
              f"Sisa Slot Kosong  : {self.sisaSlotKosong()}\n")
        for i, s in enumerate(self.sepatu, start=1):
            print(f">> Sepatu {i}\n{s.detailSepatu()}\n")
            
