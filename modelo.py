import random
import matplotlib.pyplot as plt

class Vida:
    def __init__(self):
        self.estados = ["Nacimiento", "Infancia", "Adolescencia", "Adultez", "Vejez", "Muerte"]
        self.transiciones = [
            [0.0, 0.3, 0.2, 0.2, 0.1, 0.2],  # Nacimiento
            [0.0, 0.0, 0.4, 0.3, 0.2, 0.1],  # Infancia
            [0.0, 0.0, 0.0, 0.5, 0.3, 0.2],  # Adolescencia
            [0.0, 0.0, 0.0, 0.0, 0.6, 0.4],  # Adultez
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],  # Vejez
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # Muerte
        ]
        self.estado_actual = "Nacimiento"

    def transicion(self):
        indice_actual = self.estados.index(self.estado_actual)
        probabilidades = self.transiciones[indice_actual]
        siguiente_estado = random.choices(self.estados, probabilidades)[0]
        self.estado_actual = siguiente_estado

    def simular_vida(self, pasos):
        historia = [self.estado_actual]
        for _ in range(pasos):
            self.transicion()
            historia.append(self.estado_actual)
        return historia

    def graficar_vida(self, pasos):
        historia = self.simular_vida(pasos)
        plt.figure(figsize=(10, 5))
        plt.plot(range(pasos + 1), historia)
        plt.xticks(range(pasos + 1))
        plt.yticks(range(len(self.estados)), self.estados)
        plt.xlabel("Tiempo")
        plt.ylabel("Estado de Vida")
        plt.title("Simulación de la Vida")
        plt.show()

# Ejemplo de uso
vida = Vida()
vida.graficar_vida(50)
