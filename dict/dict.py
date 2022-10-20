#Decalaração de um dicionário

pessoa = {"nome": "Jp", "idade": 19}

pessoa = dict(nome = "Jp", idade = 19)

pessoa["telefone"] = "0000-0000"

dados = {"nome": "Jp", "idade": 19, "telefone": "0000-0000"}

#Acessando o valores de um dicionário

dados["nome"] 
dados["idade"]
dados["telefone"]


#Atribuindo um novo valor a uma chave

dados["nome"] = "João"

#Dicionário aninhado

contatos = {
	
	"jplimag.fortal@gmail.com": {"nome": "João", "telefone": "0000-0000"},
	"maria123@gmail.com": {"nome": "MAria", "telefone": "0010-0440"},
	"ana.fortal@gmail.com": {"nome": "Ana", "telefone": "0044-4010"},
	"fwlipw@gmail.com": {"nome": "Felipe", "telefone": "0005-0000"}
}

#Acessando um dc aninhado

contatos["jplimag.fortal@gmail.com"]["telefone"] #0000-0000

#Iterando um dicionário

for chave in contatos:

    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
