/**
 * Práctica 09: Arreglos unidimensionales
 * Ejercicio 01: Comparador de vectores
 * 
 * Autor: Rodrigo Tufiño <rtufino@ups.edu.ec>
 * Fecha: 22-03-2022
 */
 
 #include <iostream>
 
 using namespace std;
 
 double comparar(int arr1[], int arr2[], size_t t);
 void imprimir(int arr[], size_t t);
 
 int main(){
	 cout << "-- COMPARADOR DE VECTORES --\n";
	 
	 // Tamaño de los vectores
	 size_t t;
	 cout << "Ingrese el tamaño de los vectores: ";
	 cin >> t;
	 
	 // Creación de arreglos
	 int v1[t];
	 int v2[t];
	 
	 // Ingreso de datos
	 cout << "\nDatos vector 1:\n";
	 for (size_t i=0; i< t; i++){
		 cout << "Ingrese elemento [" << i + 1<< "]: ";
		 cin >> v1[i];
	 }
	 
	 cout << "\nDatos vector 2:\n";
	 for (size_t i=0; i< t; i++){
		 cout << "Ingrese elemento [" << i + 1<< "]: ";
		 cin >> v2[i];
	 }
	 
	 // Impresión de resultados 
	 cout << "\nvector 1: ";
	 imprimir(v1, t);
	 cout << endl;
	 cout << "vector 2: ";
	 imprimir(v2, t);
	 cout << endl;
	 cout << "Similitud: " << comparar(v1, v2, t) << "%" << endl;
	 
	 return 0;
 }
/*
 * Compara la similitud de dos vectores
 */
double comparar(int arr1[], int arr2[], size_t t){
	int iguales = 0;
	for (size_t i=0; i< t; i++){
		if (arr1[i] == arr2[i]){
			iguales++;
		}
	}
	return ((double) iguales / t * 100);
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
