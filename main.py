from mobil import Mobil

avanza = Mobil(roda=4, tipe='manual', kecepatan= 200)

avanza. doMelaju()

sedan = Mobil(4, 'otomatis', 300)
sedan. doBelok('kanan')
print(sedan. penumpang)
sedan. isi_bensin()
#print(sedan, tipe)
#print(avanza, kecepatan)