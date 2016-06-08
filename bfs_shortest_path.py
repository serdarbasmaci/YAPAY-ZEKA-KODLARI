from collections import deque

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


def return_shortest_path(graph, current, parent_map, path=()):

	if current is None:
		distance = 0
		path_str = ''
		for city in path:
			if city == path[0]:
				from_city = city
				path_str = city + '->'
			else:
				distance += graph[from_city][city]
				from_city = city
				path_str += city + '->'
		return path_str[:-2] + ' Toplam: ' + str(distance) + 'KM'
	else:
		return return_shortest_path(graph, parent_map[current], parent_map, (current,) + path)


def bfs(from_city, to_city, graph):
	to_visit = deque([from_city])
	visited = set([from_city])
	parent_map = {from_city: None}

	while to_visit != []:
		current = to_visit.popleft()
		print(current+' sehrine gidiliyor.')

		neighbors = graph[current].keys()

		for n in neighbors:
			if n == to_city:
				parent_map[n] = current
				return return_shortest_path(graph, to_city, parent_map)

			elif n not in visited:
				parent_map[n] = current
				visited.add(n)
				to_visit.append(n)

	return None

print(bfs('Canakkale', 'Ankara', graph))


