import copy
N = 8

def tahta_olustur(N):
    tahta = []
    for y in range(N):
        tahta.append([])
        for x in range(N):
            tahta[y].append(0)
    return tahta

ilk_durum = {'vezirler': []}
kuyruk = [ilk_durum]
index  = 0

while True:
    if index >= len(kuyruk):
        break

    islenen = kuyruk[index]
    #print(islenen)
    if len(islenen['vezirler']) == N:
        yazdir = tahta_olustur(N)
        for vezir in islenen['vezirler']:
            yazdir[vezir['y']][vezir['x']] = 1

        for y in range(N):
            line = ""
            for x in range(N): 
                line += " " + str(yazdir[y][x])
            print(line)
        break

    tahta = tahta_olustur(N)
    for vezir in islenen['vezirler']:
        for y in range(N):
            for x in range(N):
                if x == vezir['x'] or y == vezir['y'] or x - y == vezir['x'] - vezir['y'] or x + y == vezir['x'] + vezir['y']:
                    tahta[y][x] = 1

    bulundu = False
    for y in range(N):
        for x in range(N):
            if tahta[y][x] == 0:
                yeni_durum = copy.deepcopy(islenen)
                yeni_durum['vezirler'].append({'x': x, 'y': y})
                kuyruk.insert(index+1, yeni_durum)
                #bulundu = True
        if bulundu:
            break

    index = index + 1
