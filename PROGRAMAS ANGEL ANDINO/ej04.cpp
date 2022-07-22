/**
 * Práctica 09: Arreglos unidimensionales
 * Ejercicio 04: Reservas de los asientos de un avión	 	
 * 
 * Autor: Rodrigo Tufiño <rtufino@ups.edu.ec>
 * Fecha: 22-03-2022
 */
 
 #include <iostream>
 #include <array>
 #include <iomanip>
 
 #define CAPACIDAD 18 
 
 using namespace std;
 
 int menu();
 void mostrar();
 void reservar();
 
 array<char, CAPACIDAD> asientos;
 
 int main (){
	 cout << "-- RESERVAS DE ASIENTOS --\n";
	 
	 asientos.fill('O');
	 
	 int opcion = 0;
	 do {
		 opcion = menu();
		 
		 switch(opcion){
			 case 1:
				mostrar();
				break;
			 case 2:
				reservar();
				break;
			 case 3:
				cout << "\n** FIN DEL PROGRAMA **" << endl;
				break;
		 }
	}while(opcion != 3);
	 
	 return 0;
 }
 
 int menu(){
	 int opc = 0;
	 while (1) {
		 cout << "\nMENU PRINCIPAL\n";
		 cout << "1) Mostrar asientos" << endl;
		 cout << "2) Reservar un asiento" << endl;
		 cout << "3) Salir" << endl;
		 cout << "Ingrese su opción: ";
		 cin >> opc;
		 if (opc < 1 || opc > 3){
			 cout << "¡Opción incorrecta!" << endl;
			 continue;
		 }
		 break;
	 }
	 return opc;
 }
 
 void mostrar(){
	 cout << "\nMOSTRAR ASIENTOS\n";
	 for(size_t i=0; i < asientos.size(); i++){
		 cout << setw(3) << (i+1) << ": [" << asientos[i] << "]\t";
		 if ((i+1)%2 == 0) cout << endl;
	 }
	 //cout << endl;
 }
 
 void reservar() {
	 cout << "\nRESERVAR ASIENTO\n";
	 int asiento = 0;
	 bool valido = false;
	 do {
		 cout << "Asiento: ";
		 cin >> asiento;
		 if (asiento < 1 || asiento > CAPACIDAD){
			 cout << "¡El asiento ingresado está incorrecto!" << endl;
			 continue;
		 }
		 valido = true;
	 }while(!valido);
	 
	 if (asientos[asiento-1] == 'X'){
		 cout << "El asiento ya se encuentra ocupado" << endl;
	 }else {
		 cout << "Asiento " << asiento << " reservado" << endl;
		 asientos[asiento-1] = 'X';
	 }
 }
