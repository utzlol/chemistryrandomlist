import json, requests, os

source = requests.get("https://raw.githubusercontent.com/utzlol/chemistryrandomlist/main/elementsdatabase.json")
source = source.json()

while True:
	nomor = input("Nomor : ")
	nomor = int(nomor) - 1
	chemisdet = source["elements"]
	chemisdet = chemisdet[nomor]
	print('\n')
	print(f'{chemisdet["name"]} [{chemisdet["symbol"]}] \n')
	print(f'{chemisdet["shells"]} \n')
	print(f'{chemisdet["electron_configuration"]} \n')
	print(f'{chemisdet["electron_configuration_semantic"]} \n\n')
	input('')
	os.system('clear')

