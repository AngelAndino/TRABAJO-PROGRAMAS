Algoritmo sin_titulo
	Escribir "Ingrese el número de chocolates fabricados en un día:"
	leer chocolates
	cajas<-trunc(chocolates/15)
	sobrantes<-chocolates mod 15
	Escribir "El número de cajas es:",cajas
	Escribir "Los sobrantes son:", sobrantes
FinAlgoritmo
