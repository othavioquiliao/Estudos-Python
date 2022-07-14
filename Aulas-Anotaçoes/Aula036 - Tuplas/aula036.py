tupla = ("Othavio", "Danny", "Eduardo")
print(tupla)
print(len(tupla))

tupla2 = ("Carro",) # TUPLA PRECISA DE UMA VIRGULA CASO SEJA 1 OBS SO 
print (type(tupla2))

tupla3 = ("carro") # NAO É TUPLA
print (type(tupla3))

tupla4 = tuple(("Laranja", 25 , True)) # Usando o construtor
print (tupla4)
print (type(tupla4))