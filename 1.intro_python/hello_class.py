class Carro:

    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.cilindrada = cilindrada
        self.kilometraje = kilometraje

    def encender(self):
        self._iniciar_motor()
        print("brum brum")
    
    def _iniciar_motor(self):
        print("iniciando motor...")

carro = Carro("subaru", 1500, 20000)
carro.encender()

print(f"marca carro1: {carro.marca}")

carro2 = Carro("toyota", 2000, 40000)
print(f"marca carro2: {carro2.marca}")
