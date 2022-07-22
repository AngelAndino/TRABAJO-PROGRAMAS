Algoritmo CalculoPrecios
	Escribir "Ingrese las horas:"
	Leer horas
	Escribir "Ingrese precio:"
	Leer precio
	bruto<-horas*precio
	tasas<-0.25*bruto
	neto<-bruto-tasas
	Escribir "El salario bruto es:", bruto
	Escribir "Las tasas son:",tasas
	Escribir "EL salario neto es:",neto
FinAlgoritmo
