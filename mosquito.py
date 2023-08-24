import time

class Mosquito:
    def __init__(self):
        self.etapa = "Huevo"
    
    def pasar_a_larva(self):
        if self.etapa == "Huevo":
            print("El mosquito ha eclosionado y se convierte en larva.")
            self.etapa = "Larva"
        else:
            print("No se puede convertir a larva en esta etapa.")
    
    def pasar_a_pupa(self):
        if self.etapa == "Larva":
            print("La larva se ha desarrollado y se convierte en pupa.")
            self.etapa = "Pupa"
        else:
            print("No se puede convertir a pupa en esta etapa.")
    
    def eclosionar_adulto(self):
        if self.etapa == "Pupa":
            print("La pupa ha eclosionado y se convierte en mosquito adulto.")
            self.etapa = "Mosquito Adulto"
        else:
            print("No se puede eclosionar a mosquito adulto en esta etapa.")
    
    def mostrar_etapa(self):
        print(f"El mosquito está en la etapa: {self.etapa}")


# Crear un mosquito
mosquito = Mosquito()

# Mostrar la etapa inicial
mosquito.mostrar_etapa()

# Progresión de etapas
mosquito.pasar_a_larva()
time.sleep(2)  # Simula el tiempo que lleva desarrollarse como larva
mosquito.pasar_a_pupa()
time.sleep(2)  # Simula el tiempo que lleva desarrollarse como pupa
mosquito.eclosionar_adulto()

# Mostrar la etapa final
mosquito.mostrar_etapa()
