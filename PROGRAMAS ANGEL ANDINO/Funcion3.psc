Algoritmo sin_titulo
	Escribir "Ingrese un número"
	Leer x
	r1<-RC((x^2) + (2*x) + 1)
	r2<-exp(RC(x^3))
	Respuesta <- ln(r1)/r2
	Escribir "La respuesta es:",Respuesta
FinAlgoritmo