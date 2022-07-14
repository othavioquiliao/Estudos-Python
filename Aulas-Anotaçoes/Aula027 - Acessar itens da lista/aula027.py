lista = ["Othavio", "Danny", "Arthur", "Paulo", "Joao", "Maria","Marcos"]
#Acessar itens da lista
print(lista[1])

#colocar itens da lista em variaveis
nome = lista[0]
print(nome)

#ACESSAR ALGUNS ITENS DENTRO DA LISTA
print(lista[2:5]) # DO INDICE 2 ATE O 4, ELE EXCLUI O ULTIMO

print(lista[:6]) # O primeiro e o ultimo indice nao precisa ser especificado
print(lista[0:]) # Se tu quer um indice de X local ate o final ou inicio no caso


#vERIFICAR ITENS NA LISTA
if "Othavio" in lista:
    print("O Othavio esta na lista de chamada!")
