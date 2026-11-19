import math

# luas lingkaran
def lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# luas segitiga 
def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# luas persegi
def persegi(sisi):
    return sisi ** 2

#luas kubus 
def kubus(sisi):
    return 6 * (sisi ** 2)

#luas balok 
def balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

#luas permukaan tabung
def tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

