/**
 * Práctica 09: Arreglos unidimensionales
 * Ejercicio 03: Histograma
 * 
 * Autor: Rodrigo Tufiño <rtufino@ups.edu.ec>
 * Fecha: 22-03-2022
 */
 
 #include <iostream>
 #include <stdlib.h>
  
 using namespace std;
 
 void imprimir(int arr[], size_t t);
 
 int main(){
	 cout << "-- HISTOGRAMA --\n";
	 
	 // Tamaño de  la lista
	 int min, max = 0;
	 cout << "Ingrese el rango [min max]: ";
	 cin >> min >> max;
	 
	 size_t n;
	 cout << "Ingrese el tamaño de la lista: ";
	 cin >> n;
	 	 
	 // Creación de la lista
	 int aleatorios[n];
	 
	 // Creación de histograma
	 int rango =  max - min + 1;
	 int histograma[rango] = {0};
	 
	 // Generar números aleatorios
	 int numero = 0;
	 for (size_t i=0; i< n; i++){
		 numero = min + (rand() % rango);
		 aleatorios[i] = numero;
		 histograma[numero-min]++;
	 }
	 
	 // Imprimir resultados
	 cout << "\nVector: ";
	 imprimir(aleatorios, n);
	 cout << endl;
	 // Generar histograma
	 for (int i=0; i<rango; i++){
		 cout << "[" << min + i << "]: "; 
		 for (int j=0; j < histograma[i]; j++){
			 cout << "* ";
		 }
		 cout << endl;
	 }
	 
	 return 0;
 }

/*
 * Imprime los datos de un vector
 */
void imprimir(int arr[], size_t t){
	cout << "[ ";
	for (size_t i=0; i< t; i++){
		cout << arr[i] << " ";
	}
	cout << "]";
}



