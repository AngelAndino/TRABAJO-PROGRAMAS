Algoritmo sin_titulo
	Escribir "Ingrese un Número"
	Leer num
	var<-1
	acu<-0
	Para i<-1 Hasta num Con Paso 1 Hacer
		Escribir var
		acu<-acu+var
		var<-2*var
	Fin Para
	Escribir "La suma es:",acu
FinAlgoritmo
