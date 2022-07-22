/**
 * Práctica 09: Arreglos unidimensionales
 * Ejercicio 05: Registro de calificaciones
 * 
 * Autor: Rodrigo Tufiño <rtufino@ups.edu.ec>
 * Fecha: 22-03-2022
 */
 
 #include <iostream>
 #include <iomanip>
 
 using namespace std;
 
 
 int main (){
	 cout << "-- REGISTRO DE CALIFICACIONES --\n";
	 
	 size_t n = 0;
	 cout << "Número de estudiantes: ";
	 cin >> n;
	 
	 int calificaciones[n];
	 string nombres[n];
	 
	 double suma;
	 
	 for (size_t i=0; i<n; i++) {
		 cout << "\nEstudiante " << (i+1) << endl;
		 cout << "Nombre: ";
		 cin >> nombres[i];
		 cout << "Calificación: ";
		 cin >> calificaciones[i];
		 suma += calificaciones[i];
	 }
	 
	 double promedio = suma / n;
	 cout << "\n\nCUADRO DE CALIFICACIONES\n";
	 cout << setw(4) << left << "No."; 
	 cout << setw(10) << left << "Nombre";
	 cout << setw(10) << left << "Nota";
	 cout << setw(11) << left << "Observación" << endl;
	 for (size_t i=0; i<n; i++) {
		 cout << setw(4) << left << (i+1);
		 cout << setw(10) << left << nombres[i];
		 cout << setw(10) << left << calificaciones[i];
		 cout << setw(11) << left << (calificaciones[i] > promedio ? '*' : ' ') << endl; 
	 }
	 
	 cout << "Promedio: " << promedio << endl;
	 
	 return 0;
 }
 
