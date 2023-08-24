Algoritmo Movimiento_Diaphorina
	// Variables
	Definir Diaphorina_viva,Diaphorina_Comio,Diaphorina_Ovulo,Hay_Flores_cerca Como Logico
	Diaphorina_viva <- Verdadero
	Diaphorina_Comio <- Falso
	Diaphorina_Ovulo <- Falso
	
	Mientras Diaphorina_viva Hacer
		Si No Hay_Flores_cerca Entonces
			MoverseAleatoriamente
			Hay_Flores_cerca <- HayFloresCerca
			Si Hay_Flores_cerca Entonces
				Comer
				Diaphorina_Comio <- Verdadero
			FinSi
			
		FinSi
		
		Si Diaphorina_Comio y NO Diaphorina_Ovulo Entonces
			Ovodepositar
			Diaphorina_Ovulo <- Verdadero
		FinSi
		
		si Diaphorina_Comio y Diaphorina_Ovulo Entonces
			MoverseAleatoriamente
			Diaphorina_Ovulo <- Falso
		FinSi
		
	FinMientras
	
FinAlgoritmo
SubProceso MoverseAleatoriamente
	// acciones 
FinSubProceso

Funcion HayFloresCerca
    // Acciones para verificar si hay comida cerca
    // Devuelve Verdadero o Falso
	
FinFuncion

SubProceso Comer
    // Acciones para comer
FinSubproceso

SubProceso Ovodepositar
	// Acciones para reproducirse
FinSubproceso