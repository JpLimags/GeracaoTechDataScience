#copy 

#Tem um comportamento identico ao das outras estruturas, gerando uma cópia do dicionário.

contatos = {
	
	"maria123@gmail.com": {"nome": "MAria", "telefone": "0010-0440"},
}

copia = contatos.copy()
copia["maria123@gmail.com"] = {"nome": "Ma"}


contatos["maria123@gmail.com"] #{"nome": "Maria", "telefone": "0010-0440"}

copia["maria123@gmail.com"] #{"nome": "Ma"}


#fromkeys

#Cria chaves em duas situações, quando você quer criar chaves com valores vazios, ou criar chaves padrões

dict.fromkeys(["nome", "telefone"]) #{"nome": "None", "telefone": "None"}
 
dict.fromkeys(["nome", "telefone"], "vazio") #{["nome", "telefone"], "vazio"}



#get 

contatos["chave"] #KeyError

contatos.get("chave") #none
contatos.get("chave", {}) #{}
contatos.get("maria123@gmail.com", {}) #"maria123@gmail.com": {"nome": "MAria", "telefone": "0010-0440"}

#items

#Nos retorna os items que estõ neste dicionário

contatos.items() #dict_items([("maria123@gmail.com": {"nome": "Maria", "telefone": "0010-0440"})])


#pop

contatos.pop("maria123@gmail.com") #{"nome": "Maria", "telefone": "0010-0440"}

contatos.pop("maria123@gmail.com", {}) #{}

#popitem

contatos.popitem("maria123@gmail.com") #("maria123@gmail.com": {"nome": "Maria", "telefone": "0010-0440"})
contatos.popitem() #KeyError

#setdefault 

contatos.setdefault = {"nome", "Joana"} #"Maria"
contatos #{"nome": "Maria", "telefone": "0010-0440"}}

contatos.setdefault = {"idade", "28"}

#update

contatos.update = ({"maria123@gmail.com": {"nome": "Ma"}}) #"Maria"
contatos #{"maria123@gmail.com": "nome": "Ma"}

contatos.update = ({{"jplimag.fortal@gmail.com": {"nome": "João", "telefone": "0000-0000"}}}) #"Maria"
contatos #{"maria123@gmail.com": {"nome": "MAria", "telefone": "0010-0440"}, "jplimag.fortal@gmail.com": {"nome": "João", "telefone": "0000-0000"}

#Values
#Retorna os valores que estão inseridos no dicionário

contatos.values() ## contatos = {	
#	"jplimag.fortal@gmail.com": {"nome": "João", "telefone": "0000-0000"},
#	"maria123@gmail.com": {"nome": "MAria", "telefone": "0010-0440"},
#	"ana.fortal@gmail.com": {"nome": "Ana", "telefone": "0044-4010"},
#	"fwlipw@gmail.com": {"nome": "Felipe", "telefone": "0005-0000"}
#}