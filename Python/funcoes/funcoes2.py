#Args e kwargs

def exibir_poema(data_extenso, *args, **kwargs):

    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave , valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Is best languagem of promaming", autor="Tim Peters", ano = 1999)


#Keyword and Positional only

def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Corsa", 2002, "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina") #valido
criar_carro(modelo="Corsa", ano = 2002, placa = "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina")  #inválido

#keyword only

def criar_carro(*,modelo, ano, placa, marca, motor, combustivel ):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Corsa", ano = 2002, placa = "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina") #válido 
criar_carro("Corsa", 2002, "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina") #invalido

#keyboard and positional only

criar_carro("Corsa", 2002, "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina") #Invalido
criar_carro(modelo="Corsa", ano = 2002, placa = "ABC-1234", marca="Chevrolet", motor=1.0, combustivel= "Gasolina") #Valido


#Funcoes como objetos de primeira classe

def somar(a,b):
    return a+b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

print(exibir_resultado(10,10,somar))