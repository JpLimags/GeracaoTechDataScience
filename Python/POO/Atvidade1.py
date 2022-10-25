
class Bicicletaria:

    def __init__(self, cor, modelo, ano, valor, buzinar = True, parar = True, correr = True):

        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.buzinar = buzinar
        self.parar = parar
        self.correr = correr
    
    def buzinar(self):
        if self.buzinar == False:
            print("A bicicleta não tem buzina")
        else:
            print("A bicicleta tem buzina")

    def parar(self):

        self.parar = False
        print("A bike tá sem freio  melhor trocar")


    def correr(self):

        self.correr = False
        print("Pneu furado menor !")

bike1 = Bicicletaria("Azul", "Monark", 2016,1200, False, True, True)


print(bike1.ano)


    