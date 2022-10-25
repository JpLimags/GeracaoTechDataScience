#declarando uma função no python

def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}")


exibir_mensagem()
exibir_mensagem_2("João")
exibir_mensagem_3()

print("----"*20)

#Retornando valores

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numeros):
    
    antecessor = numeros - 1
    sucessor = numeros + 1

    return antecessor, sucessor

print(calcular_total([10,15,20]))
print(retorna_antecessor_sucessor(15))

#Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):

    print(f"Carro inserido com sucesso ! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Chevrolet", "Corsa", 2002, "ABC-1584")
salvar_carro(marca="Chevrolet", modelo="Corsa", ano=2002, placa="ABC-1584")
salvar_carro(**{"marca": "Chevrolet", "modelo": "Corsa", "ano": 2002, "placa": "ABC-1584"})