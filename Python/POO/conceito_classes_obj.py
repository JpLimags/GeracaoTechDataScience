#Ex: calsse e obj

class Cachorro:
    
    def __init__(self, nome, cor, acordado = True):
        
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("AuAu")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzzz...")

#Objetos:

cao1 =  Cachorro("Pichula", "caramelo", False)

print(cao1.acordado)
