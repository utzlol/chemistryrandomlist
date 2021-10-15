import json, requests

source = requests.get("https://raw.githubusercontent.com/utzlol/chemistryrandomlist/main/elementsdatabase.json")
source = source.json()

while True:
	nomor = input("Nomor : ")
	nomor = int(nomor) - 1
	chemisname = source["elements"]
	chemisname = chemisname[nomor]
	print('\n')
	print(chemisname["name"] +"  "+ chemisname["electron_configuration"]+"\n")
