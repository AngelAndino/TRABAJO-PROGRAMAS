Algoritmo sin_titulo
	Escribir "Ingrese la cantidad de calificaciones"
	Leer n
	i<-1
	acu<-0
	Mientras i<=n Hacer
		Escribir "Ingrese la calificación:"
		Leer cal
		acu<-acu+cal
		i<-i+1
	Fin Mientras
	Escribir "La suma es:",acu
	Escribir "El promedio es:",acu/n
FinAlgoritmo
