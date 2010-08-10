#-*-coding:utf:8-*-
import sys , os

dosya_yeri = raw_input("dosyanın yeri : ")
yeni_ad1 = raw_input("düzeltildikten sonraki yeni adresi : ")

if not os.path.isdir(yeni_ad1):
	print "verilen adres doğru değil."
	sys.exit()

yeni_ad2 = raw_input("düzeltildikten sonraki yeni adı : ")

hps = []

if yeni_ad1[len(yeni_ad1) - 1] == "/":
	yeni_ad = yeni_ad1 + yeni_ad2
else:
	yeni_ad = yeni_ad1 + "/" + yeni_ad2


try:
	dosya = open(dosya_yeri,"r")
except IOError:
	print "'%s' dosyası açılamıyor" %dosya_yeri
	sys.exit()
	
	
yedek = open("/home/eroluslu/yedek.txt","w+r")
satir = dosya.readlines()
satir_sayisi = len(satir)
dosya.seek(0)



try:
	bir = satir[0].index(".") + 1
	merkez = "."
except ValueError:
	iki = 0
	while ((satir[0][iki] != " ") ) & (iki <= len(satir[0])):
		iki += 1
	merkez = satir[0][iki]
	bir = iki
 


while ((satir[0][bir] == " ") | (satir[0][bir] == "\t")) & (bir <= len(satir[0])):
	bir += 1
	


bir -= satir[0].index(merkez)
max_tab_uzunluk = 0

for i in range(satir_sayisi):	
	ara = satir[i][satir[i].index(merkez) + bir :]
	if len(ara) == 0:
		ara = " \n"
	k = 0
	say = 0
	j = 0
	while ((ara[say] == ' ') | (ara[say] == '\t')) & (say <= len(ara)):
		if ara[say] == ' ':
			j += 1
		elif ara[say] == '\t':
			k += 1
		say += 1
	j += k * 4
	hps.append([j,ara])
	if (max_tab_uzunluk < hps[len(hps) - 1][0] - hps[len(hps) - 2][0]) & (hps[len(hps) - 1][0] > hps[len(hps) - 2][0]):
		max_tab_uzunluk = abs(hps[len(hps) - 1][0] - hps[len(hps) - 2][0])

hps.insert(0,[0,"#-*-coding:utf:8-*-\n"])
yedek.write("#-*-coding:utf:8-*-\n")
tab_mik = []


for i in range(len(hps)):
	tab_mik.append(0)

for i in range(1,len(hps)):
	if hps[i][0] > hps[i - 1][0]:
		tab_mik[i] = tab_mik[i - 1] - 1
	elif hps[i][0] < hps[i - 1][0]:
		tab_mik[i] = tab_mik[i - 1] + (hps[i][0] - hps[i - 1][0]) / max_tab_uzunluk
print max_tab_uzunluk

for i in range(1,len(hps)):
	ara2 = ""
	for f in range(tab_mik[i]):
		ara2 = ara2 + "\t"
	ara2 = ara2 + hps[i][1]
	yedek.write(ara2)
	

os.rename("/home/eroluslu/yedek.txt",yeni_ad)
print "%s dosyası hazır"%os.path.basename(yeni_ad)

dosya.close()
yedek.close()
