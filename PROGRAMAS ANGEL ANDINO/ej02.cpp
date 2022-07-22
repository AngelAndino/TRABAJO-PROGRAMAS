/**
 * Práctica 09: Arreglos unidimensionales
 * Ejercicio 02: Calculos estadísticos
 * 
 * Autor: Rodrigo Tufiño <rtufino@ups.edu.ec>
 * Fecha: 22-03-2022
 */
 
 #include <iostream>
 #include <cmath>
 
 using namespace std;
 
 void imprimir(double arr[], size_t t);
 double media(double arr[], size_t t);
 double varianza(double arr[], size_t t);
 
 int main(){
	 cout << "-- CALCULOS ESTADÍSTICOS --\n";
	 
	 // Tamaño de  la lista
	 size_t n;
	 cout << "Ingrese el tamaño de la lista: ";
	 cin >> n;
	 
	 // Creación de la lista
	 double lista[n];
	 
	 // Ingreso de datos
	 cout << "\nIngrese la lista de números:\n";
	 for (size_t i=0; i< n; i++){
		 cout << "Elemento [" << i + 1<< "]: ";
		 cin >> lista[i];
	 }
	 	 
	 // Calculos 
	 double x = media(lista, n);
	 double var = varianza(lista, n);
	 double dStd = sqrt(var);
	 
	 // Impresion	 
	 cout << "\nLista: ";
	 imprimir(lista, n);
	 cout << endl;
	 cout << "Media = " << x << endl;
	 cout << "Varianza = " << var << endl;
	 cout << "Desviación estándar = " << dStd << endl;
	 
	 return 0;
 }

/*
 * Imprime los datos de un vector
 */
void imprimir(double arr[], size_t t){
	cout << "[ ";
	for (size_t i=0; i< t; i++){
		cout << arr[i] << " ";
	}
	cout << "]";
}

double media(double arr[], size_t n){
	double suma = 0;
	for (size_t i=0; i < n; i++){
		suma += arr[i];
	}
	return suma / n;
}

double varianza(double arr[], size_t n){
	double x = media(arr, n);
	double suma = 0;
	for (size_t i=0; i < n; i++){
		suma += pow(arr[i] - x, 2);
	}
	return suma / n;
}


