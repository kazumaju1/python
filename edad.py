'''decir cuantos años tiene una persona, pidiendo la fecha de su nacimiento y comparandola con el 15/6/2022'''

dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
edad = 2022 - año

if mes < 6 :
	print(edad)		
elif mes == 6 :
	if dia > 15 :
		print(edad - 1)
	else :
		print(edad)
else :
	print(edad-1)
