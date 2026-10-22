
class KatakZuma:
    def __init__(self, warna_peluru):
        self.warna_peluru = warna_peluru
        self.skor = 0
        self.bola = []

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru

    def tembak(self):
        self.bola.append(self.warna_peluru)
        print("Menembak bola", self.warna_peluru)

        if len(self.bola) >= 3:
            if self.bola[-1] == self.bola[-2] == self.bola[-3]:
                self.skor += 50
                del self.bola[-3:]
                print("3 bola sama! Skor +50")

    def info_status(self):
        print("Warna peluru:", self.warna_peluru)
        print("Rantai bola:", self.bola)
        print("Skor:", self.skor)


# --- Simulasi Pertarungan ---
katak_player = KatakZuma("Biru")

katak_player.tembak()
katak_player.tembak()
katak_player.tembak()

katak_player.info_status()

katak_player.ganti_warna("Merah")

katak_player.info_status()