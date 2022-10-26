
class Bicicletaria:

    def __init__(self, cor, modelo, ano, valor):

        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
            print("bi bi...")
    
    def parar(self):

    
        print("Freiando a bicileta")


    def correr(self):

        print("Zuuuuuuuum...")

bike1 = Bicicletaria("Azul", "Monark", 2016,1200)


print(bike1.ano)


    