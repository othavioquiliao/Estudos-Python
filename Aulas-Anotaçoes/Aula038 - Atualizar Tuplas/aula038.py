x = ("Othavio", "Danny", "Arthur")
print(x)

# ALTERAR ITEM
y = list(x) # Converte a tupla em lista
y[1] = "Daniel" # Altera o item na lista criada
x = tuple(y) # Converte a lista em tupla novamente
print(x)

# ADICIONAR ITEM 1x
y = list(x)
y.append("Jonas")
x = tuple(y)
print(x)

# ADICIONAR ITEM MELHOR JEITO
t = ("Marcos", "Rose") #Cria uma nova tupla soma com a outra
x += t
print(x)

#REMOVER ITENS
j = list(x) # Mesma soluçao tu converte em lista e usa ".remove"
j.remove("Marcos")
x = tuple(j)
print(x)

# DELETAR A TUPLA COMPLETAMENTE
del x
print(x)

