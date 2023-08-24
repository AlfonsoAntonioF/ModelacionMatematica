import numpy as np
import matplotlib.pyplot as plt
import random


class parche:
    # creacion del objeto 
    def __init__(self,coordenadas, humedad, temperatura,id_parche):
        print('Creando parche: %s' % str(id_parche))
        #Atributos
        self.coordenadas = coordenadas
        self.humedad = humedad
        self.temperatura = temperatura
        self.id_parche = id_parche
    
    
class Huevo:
    # creacion del objeto huevo
    def __init__(self,id_huevo ,estado_huevo ,posicion_huevo):
        print('Creando huevo: %s' % str(id_huevo))
        self.id_huevo = id_huevo
        self.estado_huevo = estado_huevo
        self.posicion_huevo = posicion_huevo
    

class Mosquito_Hembra:
    #creacion del objeto Mosquito_Hembra
    def __init__(self,id_Mosquito_Hembra, Estado_Mosquito_Hembra,Edad_Mosquito_Hembra,Posicion_Mosquito_Hembra):
        print('Creando Mosquito_Hembra: %s' % str(id_Mosquito_Hembra))
        self.id_Mosquito_Hembra = id_Mosquito_Hembra
        self.Estado_Mosquito_Hembra = Estado_Mosquito_Hembra
        self.Edad_Mosquito_Hembra = Edad_Mosquito_Hembra
        self.Posicion_Mosquito_Hembra = Posicion_Mosquito_Hembra

Matriz_Transiciones = [
            [0.0, 0.3, 0.2, 0.2],  # Viable
            [0.0, 0.0, 0.4, 0.3],  # Latencia
            [0.0, 0.0, 0.0, 0.5],  # Adulto_Hembra
            [0.0, 0.0, 0.0, 0.0]  # Muerte
            
        ]    