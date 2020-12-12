

def main():
	file = open("inputDay1.txt","r")
	precios= []
	for line in file:
		precios.append(int(line))
	file.close()


	#buscaPrecio2(precios)
	buscaPrecio3(precios)


def buscaPrecio2(precios):
	completados = []
	for precio in precios:

		try:# acceso al valor para que sea O(n)
			try:# se comprueba que no este repetida

				completados.index(precio) and completados.index((2020-precio))

			except ValueError:
				if precios.index((2020-precio)):
					completados.append(int(precio))
					completados.append(int(2020-precio))
					print(precio*(2020-precio))
							
		except ValueError:
			continue

def buscaPrecio3(precios):
	completados = []
	for precio1 in precios:

		for precio2 in precios:

			for precio3 in precios:
				try:					#para quitar repetidos
					completados.index(precio1) and completados.index(precio2) and completados.index(precio3)

				except ValueError:
					if precio1 != precio2 and precio1 != precio3 and precio2 != precio3 and (precio1 + precio2 + precio3) == 2020:
					 	completados.append(int(precio1))
					 	completados.append(int(precio2))
					 	completados.append(int(precio3))
					 	print(precio1*precio2*precio3)

main()