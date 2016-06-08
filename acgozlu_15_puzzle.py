import copy
import math

def sirali_mi(tahta ,N):
	for y in range(N):
		for x in range(N):
			eleman = tahta[y][x]
			if (y < N - 1 or x < N - 1) and eleman != y * N + x + 1:
				return False
	return True

def fark_hesapla(tahta ,N):
	fark = 0.0
	for y in range(N):
		for x in range(N):
			eleman = tahta[y][x]
			
			if eleman == 0:
				olmasi_gereken_x = N - 1
				olmasi_gereken_y = N - 1
			else:
				eleman = eleman - 1
				olmasi_gereken_x = eleman % N
				olmasi_gereken_y = int((eleman - olmasi_gereken_x) / N)

			delta_x = abs(olmasi_gereken_x - x)
			delta_y = abs(olmasi_gereken_y - y)

			fark = fark + math.sqrt(delta_x ** 2 + delta_y ** 2)
	return fark

def hamle_ismi(i):
	if i == 0:
		return "Yukaridan Asagi"
	if i == 1:
		return "Asagidan Yukari"
	if i == 2:
		return "Soldan Saga"
	if i == 3:
		return "Sagdan Sola"

def sifir_pozisyonu(tahta, N):
	for y in range(N):
		for x in range(N):
			if tahta[y][x] == 0:
				return (x, y)

def main():
	N = 3
	durum = {'tahta': [[5,0,6], [8,1,3], [4, 7, 2]], 'hamle': []}

	kuyruk = [durum]
	index = 0
	while True:
		islenen = kuyruk[index]
		print(islenen)
		if sirali_mi(islenen['tahta'], N):
			# Hamleleri yaz.
			print(" -> ".join(map(hamle_ismi, islenen['hamle'])))
			break

		x, y = sifir_pozisyonu(islenen['tahta'], N)

		if len(islenen['hamle']) > 0:
			son_hamle = islenen['hamle'][-1]
			#son_hamle = -1
		else:
			son_hamle = -1

		secenekler = []

		if y > 0 and son_hamle != 1:
			# Usttekini asagi cekme
			yeni_durum = copy.deepcopy(islenen)
			yeni_durum['hamle'].append(0)
			yeni_durum['tahta'][y-1][x] = 0
			yeni_durum['tahta'][y][x] = islenen['tahta'][y-1][x]
			secenekler.append({'durum': yeni_durum, 'fark': fark_hesapla(yeni_durum['tahta'], N)})
		if x > 0 and son_hamle != 3:
			# Soldakini saga cekme
			yeni_durum = copy.deepcopy(islenen)
			yeni_durum['hamle'].append(2)
			yeni_durum['tahta'][y][x-1] = 0
			yeni_durum['tahta'][y][x] = islenen['tahta'][y][x-1]
			secenekler.append({'durum': yeni_durum, 'fark': fark_hesapla(yeni_durum['tahta'], N)})
		if y < N-1 and son_hamle != 0:
			# Alttakini uste cekme
			yeni_durum = copy.deepcopy(islenen)
			yeni_durum['hamle'].append(1)
			yeni_durum['tahta'][y+1][x] = 0
			yeni_durum['tahta'][y][x] = islenen['tahta'][y+1][x]
			secenekler.append({'durum': yeni_durum, 'fark': fark_hesapla(yeni_durum['tahta'], N)})
		if x < N-1 and son_hamle != 2:
			# Sagdakini sola cekme
			yeni_durum = copy.deepcopy(islenen)
			yeni_durum['hamle'].append(3)
			yeni_durum['tahta'][y][x+1] = 0
			yeni_durum['tahta'][y][x] = islenen['tahta'][y][x+1]
			secenekler.append({'durum': yeni_durum, 'fark': fark_hesapla(yeni_durum['tahta'], N)})
		
		secilen = 0
		for i in range(len(secenekler)):
			if secenekler[i]['fark'] < secenekler[secilen]['fark']:
				secilen = i
		kuyruk.append(secenekler[i]['durum'])

		index = index + 1

if __name__ == "__main__":
    main()