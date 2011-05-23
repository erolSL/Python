#!/usr/bin/python
# -*- coding: utf-8 -*-

# Bu program verileri banka.gir dosyasından alır.
# banka.gir adinda dosyamizin icerigi ;
# 		3 --> okunacak asal sayi miktari
# 		3 7 13 --> verilen asal sayilar
# 		5 --> sifresi istenilen musteri numarasi
# Programda 2 liste  var. Birisinde verilen asal sayılar tutulacak, 
# diğerinde ise bu asal sayılardan oluşturulan sayılar tutulacak.
# liste'deki sayılar sırasıyla asal sayılarla çarpılıp tekrar listenin içine
# sıralı olacak şekilde eklenir. Sıralama işi sondan taranarak yapılır. 
# Bunun sebebi taranacak sayı miktarını en aza indirmek. Var olan sıralama 
# fonksiyonları tüm sayıları sıralarken aşağıdaki fonksiyonlar(ekle, sirali_ekle)
# sadece bir sayıyı sıralar ve ekler. Bu asal sayıların en küçüğü ile çarpılan sayının
# indisine göre sonlandırılır(küçük sayı ile küçük sayının çarpımı yine küçük sayıdır).
# liste'nin bir diğer özelliği ise müşteri numarası ile sınırlı olmasıdır.
# Böylece sıralama yaparken taranan sayı miktarı azaltılmış olur. 

# Sirali olacak şekilde ekleme kısmı burada yapılır.
def ekle(a):
	for i in range(len(liste) - 1, -1, -1):
		if liste[i] < a:
			liste.insert(i + 1, a)
			return (i + 1)
			

# listeyi sınırlama ve eklemeyi yönetme işi burada
def sirala_ekle(a):
	if a in liste:	# Daha onceden eklendiyse 
		return 0
	elif len(liste) < k:	# Liste sinirina ulasilmadiysa hemen ekle
		return ekle(a)
	elif liste[-1] < a: 	# Liste sinirina erisilmisse ve son elemandan buyukse
		return k
	else:
		liste.pop()
		return ekle(a)
		

girdi = open("banka.gir", "r")
dosya = girdi.readlines()
girdi.close()

liste = []	# Oluşturulan sayıların tutulduğu liste
asal_sayilar = []	# Verilen asal sayıların tutulduğu liste
k = int(dosya[2])	# Musteri numarasi

# Verilen asal sayıları alma burada
asal_sayilar = dosya[1].split(" ")

for i in range(len(asal_sayilar)):
	asal_sayilar[i] = int(asal_sayilar[i])

# Eğer asal sayılar sıralı verilmemişse diye sıralanır ve liste'ye eklenir.
asal_sayilar.sort()
liste.extend(asal_sayilar)

i = 0		# liste'de dolaşmak için

# a, en küçük asal sayı ile çarpılmış sayının indisi.
# Program bu sayı baz alınarak çalışır.
# b ise diğer asal sayılar ile çarpılmış sayıların indisini bir yere döndürmek için kullanıldı.
# Isi garantiye almak icin
while(True):
	for j in range(len(asal_sayilar)):
		if j == 0:
			a = sirala_ekle(liste[i] * asal_sayilar[j])
		else:
			b = sirala_ekle(liste[i] * asal_sayilar[j])
	i += 1
	if a >= k - 1:
		break

# Ve sifre ekrana basilir
print liste[int(dosya[2]) - 1]
