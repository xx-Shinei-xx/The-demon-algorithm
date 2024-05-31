import random
import matplotlib.pyplot as plt

class GasIdeal:
    def __init__(self, N, delta):
        self.v = [0.0] * N
        self.Energía_del_Sistema = 0.0  # Energía del sistema
        self.Energía_del_Demonio = 1.0  # Energía del demonio
        self.mcs = 0  # Número de movimientos de Monte Carlo por partícula
        self.Energía_del_Sistema_Acumulada = 0.0
        self.Energía_del_Demonio_Acumulada = 0.0
        self.Movimientos_Aceptados = 0
        self.delta = delta  # Cambio de velocidad de la partícula

    def inicializar(self):
        N = len(self.v)
        self.systemEnergy = 0.0
        for i in range(N):
            self.v[i] = 0.0  # Todas las partículas inician con la misma velocidad inicial
        self.Energía_del_Demonio = 1.0  # El demonio inicia con una energía distinta de 0
        self.resetear()

    def resetear(self):
        self.mcs = 0
        self.Energía_del_Sistema_Acumulada = 0.0
        self.Energía_del_Demonio_Acumulada = 0.0
        self.Movimientos_Aceptados = 0

    def Monte_Carlo(self): # Monte Carlo
        for _ in range(len(self.v)):
            particleIndex = random.randint(0, len(self.v) - 1) # Selecciona una partícula aleatoria
            dv = (random.random() - 0.5) * self.delta # cambia la velocidad a una aleatoria
            oldVelocity = self.v[particleIndex] # calcula el cambio de energía con la velocidad
            newVelocity = oldVelocity + dv
            dE = 0.5 * (newVelocity ** 2 - oldVelocity ** 2)
            if dE <= self.Energía_del_Demonio:
                self.v[particleIndex] = newVelocity
                self.Energía_del_Demonio -= dE
                self.Energía_del_Sistema += dE
                self.Movimientos_Aceptados += 1

        self.Energía_del_Sistema_Acumulada += self.Energía_del_Sistema
        self.Energía_del_Demonio_Acumulada += self.Energía_del_Demonio
        self.mcs += 1

N = 100  # Número de partículas
delta = 1.0  # Cambio de velocidad
n_pasos = 1000 # Número de pasos

gas_ideal = GasIdeal(N, delta)
gas_ideal.inicializar()


Valores_Energía_Del_Sistema = []
Valores_Energía_Del_Demonio = []
for _ in range(n_pasos):
    gas_ideal.Monte_Carlo()
    Valores_Energía_Del_Sistema.append(gas_ideal.Energía_del_Sistema_Acumulada / gas_ideal.mcs)
    Valores_Energía_Del_Demonio.append(gas_ideal.Energía_del_Demonio_Acumulada/ gas_ideal.mcs)


# Gráficas
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(Valores_Energía_Del_Sistema, color='blue')
plt.title('Average particle energy')
plt.xlabel('Iterations')
plt.ylabel('Average energy')
plt.subplot(1, 2, 2)
plt.plot(Valores_Energía_Del_Demonio, color='red')
plt.title('Iterations')
plt.xlabel('Iterations')
plt.ylabel('Demon´s energy')

# Mostrar las partículas en la caja inicial
plt.figure(figsize=(10, 5))
for i, v in enumerate(gas_ideal.v):
    color = 'blue' if v**2 < (sum(v**2 for v in gas_ideal.v) / len(gas_ideal.v)) else 'red'
    x = random.random()
    y = random.random()
    plt.scatter(x, y, color=color)
plt.title('Initial particle distribution ')
plt.show()

# Realizar los pasos de Monte Carlo para llegar al estado final
for _ in range(n_pasos):
    gas_ideal.Monte_Carlo()

# Mostrar las partículas en la caja final
plt.figure(figsize=(10, 5))
for i, v in enumerate(gas_ideal.v):
    color = 'blue' if v**2 < (sum(v**2 for v in gas_ideal.v) / len(gas_ideal.v)) else 'red'
    x = random.random() * 0.5 if color == 'blue' else 0.5 + random.random() * 0.5
    y = random.random()
    plt.scatter(x, y, color=color)
# Línea divisoria 
plt.axvline(x=0.5, color='black')  
plt.title('Final particle distribution')
plt.show()
