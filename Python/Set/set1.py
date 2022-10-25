#Em conjuntos não existe valores duplicados

lista1 = [1,8,5,6,3,3,5]

#Quando passarmos essa lista para um set  os valores repetidos irá sumir, e também será ordenado, neste caso mas não é algo que sempre irá se repeti

print(set(lista1))


#Iterando conjuntos

carros = {"Fusca", "Celta", "Corola"}

for carro in carros:
    print(carro)

#Para sabermos o índice de um objeto dentro do laço for, utilizamos a função enumerate
#Ex:

for indice,carro in enumerate(carros):

    print(f"{indice}: {carro}")


#Agora vamos ver algumas operações da classe set

#Union

conj1 = {7,51}
conj2 = {8,9}

print(conj1.union(conj2))

#interserction

conj1 = {2,3,4}
conj2 = {1,2,3}

print(conj1.intersection(conj2))


#difference

conj1 = {2,3,4}
conj2 = {1,2,3}

print(conj1.difference(conj2))

#symetric_difference

conj1 = {2,3,4}
conj2 = {1,2,3}

print(conj1.symmetric_difference(conj2))

#issubset

conj1 = {1,2,3}
conj2 = {4,1,5,6,2,7,8,3}

print(conj1.issubset(conj2))
print(conj2.issubset(conj1))

#issuperset

conj1 = {1,2,3}
conj2 = {4,1,5,6,2,7,8,3}

print(conj1.issuperset(conj2))
print(conj2.issuperset(conj1))

#add

sorteio = {1,4}

sorteio.add(8)
sorteio.add(16)

print(sorteio)

#clear
sorteio = {1,4}

sorteio.add(8)
sorteio.clear()

print(sorteio)

#discard
nums = {1,2,3,1,2,4,5,5,5,6,7,8,9,0}


nums.discard(1)
nums.discard(45)

print(nums)


#pop
nums = {1,2,3,1,2,4,5,5,5,6,7,8,9,0}


nums.pop()
nums.pop()

print(nums)


#remove

nums = {1,2,3,1,2,4,5,5,5,6,7,8,9,0}


nums.remove()
nums.remove()

print(nums)


#len

nums = {1,2,3,1,2,4,5,5,5,6,7,8,9,0}


print(len(nums))
