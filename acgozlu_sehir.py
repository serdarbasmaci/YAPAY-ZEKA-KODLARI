graph =  {'Canakkale': {'Izmir': 325 , 'Balikesir': 207 , 'Bursa': 271 , 'Tekirdag': 188 , 'Edirne': 217},
		  'Izmir': {'Manisa': 36 , 'Usak': 211 , 'Canakkale': 325},
		  'Balikesir': {'Manisa': 137 , 'Bursa': 151 , 'Canakkale': 207},
		  'Edirne': {'Tekirdag': 140 , 'Istanbul': 229 , 'Canakkale': 217},
		  'Manisa': {'Izmir': 36 , 'Balikesir': 137},
		  'Bursa': {'Istanbul': 243 , 'Kocaeli': 132 , 'Eskisehir': 149 , 'Balikesir': 151, 'Canakkale': 271},
		  'Tekirdag': {'Istanbul': 132 , 'Canakkale': 188 , 'Edirne': 140},
		  'Usak': {'Afyon': 116 , 'Izmir': 211},
		  'Istanbul': {'Kocaeli': 111 , 'Edirne': 229 , 'Bursa': 243 , 'Tekirdag': 132},
		  'Kocaeli': {'Eskisehir': 219 , 'Bolu': 151 , 'Istanbul': 111 , 'Bursa': 132},
		  'Eskisehir': {'Kutahya': 78 , 'Ankara': 233 , 'Kocaeli': 219 , 'Bursa': 149},
		  'Bolu': {'Ankara': 191 , 'Kocaeli': 151},
		  'Kutahya': {'Afyon': 100 , 'Eskisehir': 78},
		  'Afyon': {'Ankara': 256 , 'Usak': 116},
		  'Ankara': {'Eskisehir': 233 , 'Bolu': 191 , 'Afyon': 256}}

guzergah = ['Canakkale']
toplam_yol = 0

while guzergah[-1] != 'Ankara':
	simdiki_sehir = guzergah[-1]

	en_yakin_komsuya_uzaklik = -1
	en_yakin_komsu = ""

	for komsu in graph[simdiki_sehir]:
		if komsu in guzergah:
			print("  --  " + komsu + " sehri daha once ziyaret edildiginden atliyoruz.")
			continue
			# Bu sehire daha once geldiysek tekrar gitme.

		uzaklik = graph[simdiki_sehir][komsu]

		if en_yakin_komsuya_uzaklik == -1 or uzaklik < en_yakin_komsuya_uzaklik:
			en_yakin_komsu = komsu
			en_yakin_komsuya_uzaklik = uzaklik

	if en_yakin_komsu == "":
		print("")
		print("Ziyaret edilebilecek baska komsu kalmadi.")
		break

	print(en_yakin_komsu + " sehrine gidiliyor. Uzaklik: " + str(en_yakin_komsuya_uzaklik) + " km")
	guzergah.append(en_yakin_komsu)
	toplam_yol = toplam_yol + en_yakin_komsuya_uzaklik

print("Guzergah: " + " -> ".join(guzergah))
print("Toplam katedilen yol: " + str(toplam_yol) + "km")

