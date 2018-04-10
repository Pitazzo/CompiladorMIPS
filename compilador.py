from sys import stdin

argumentos = [""]
aritmeticas = ['add', 'addfp']
inmediato = ['lw', 'sw', 'beq']

while argumentos[0] != 'fin':
	argumentos = stdin.readline()[0:-1].split(' ')
	if argumentos[0] != 'fin':
		if len(argumentos) == 4 and (argumentos[0] in aritmeticas or argumentos[0] in inmediato):
			if argumentos[0] in aritmeticas:
				if argumentos[0] == 'add':
					salida = '000001'
				else:
					salida = '100000'
				salida = salida + ' ' \
							 + bin(int(argumentos[2][1:]))[2:].zfill(5) \
							 + ' ' + bin(int(argumentos[3][1:]))[2:].zfill(5) \
							 + ' ' + bin(int(argumentos[1][1:]))[2:].zfill(5) \
							 + ' ' + '00000000000'
				print '\t' + salida
				salida = salida.replace(' ', '')
				print '\t' + hex(int(salida, 2)).zfill(8)
			else:
				if argumentos[0] == 'lw':
					salida = '000010'
				elif argumentos[0] == 'sw':
					salida = '000011'
				elif argumentos[0] == 'beq':
					salida = '000100'
				salida = salida + ' ' + bin(int(argumentos[2][1:]))[2:].zfill(5) \
							 + ' ' + bin(int(argumentos[1][1:]))[2:].zfill(5) \
							 + ' ' + bin(int(argumentos[3]))[2:].zfill(16)
				print '\t' + salida
				salida = salida.replace(' ', '')
				print '\t' + hex(int(salida, 2)).zfill(8)
		else:
			print "ERROR"
		
