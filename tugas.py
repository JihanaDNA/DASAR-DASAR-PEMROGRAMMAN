def celcius_ke_fahrenheit(celcius):
  return(celcius * 9/5) +32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# -----------------------------------------------

def is_genap(angka):
   return angka % 2==0

print(is_genap(4))
print(is_genap(7))

# -----------------------------------------------

def nilai (angka):
  if angka >= 75:
     print("Lulus")
  else:
     print("Gagal")
nilai(80)
nilai(60)

# -----------------------------------------------

def bilangan(angka):
  for i in range(1,angka,2):
    print(i, end=',')

bilangan(20)