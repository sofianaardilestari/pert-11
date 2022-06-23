class Mobil:

    def __init__(self, roda, tipe, kecepatan):
        self, roda = roda
        self, tipe = tipe
        self, kecepatan = kecepatan
        self, penumpang = 2

    def doMelaju(self):
        print("mobile Melaju : ", self. kecepatan)


    def doBelok(self, arah):
        print('belok arah', arah)

    def doKalkson(self):
        print('klakson')