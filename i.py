def i(string):
	lista = list(string)

	for n,i in enumerate(lista):
		if i == 'a' or i == 'e' or i == 'o' or i == 'u':
			lista[n] = 'i'
		elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
			lista[n] = 'I'

	return ''.join(lista)

if __name__ == '__main__':
	entrada = input()
	print(i(entrada))