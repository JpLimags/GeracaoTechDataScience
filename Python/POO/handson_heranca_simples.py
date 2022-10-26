from calendar import c


class Veiculo:

    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print ("Ligando motor")



class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, carregado, cor, placa, numero_rodas):
        

        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


cam1 = Caminhao(True, "Azul", "ABC-1243", 4)
print(cam1.esta_carregado())


