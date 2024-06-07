# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	n = int()
	a = int()
	b = int()
	c = int()
	print("Escribe un numero")
	n = int(input())
	for a in range(n,0,-1):
		for b in range(1,a+1):
			print(" ", end="")
		for c in range(a,n+1):
			print("* ", end="")
		print("")

