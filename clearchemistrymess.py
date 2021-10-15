import requests, json

url = requests.get("https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json")
url = url.json()

url = url['elements']

num = 0

file = open('editelement.json','a')

while True:
	urlch = url[num]
	remove = ["appearance", "atomic_mass",'boil','category','color','density','discovered_by','melt','molar_heat','named_by','number','period','phase','source','spectral_img','summary','xpos','ypos','electron_affinity','electronegativity_pauling','ionization_energies','cpk-hex']
	for removeorder in remove:
		del urlch[removeorder]
	print(urlch)
	json_object = json.dumps(urlch, indent = 4) 
	file.write(json_object)
	num = num + 1
	
