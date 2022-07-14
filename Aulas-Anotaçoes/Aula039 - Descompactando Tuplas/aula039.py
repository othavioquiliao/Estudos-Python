nomes = ("Othavio", "Danny", "Arthur", "Marcos", "Roberta")
print(nomes)

#(n1, n2, n3) = nomes # Colocar as informaçoes da tupla em variaveis
#(n1, n2, *n3) = nomes # O "*" CONVERTE DOSO OS OUTROS MEMBROS DA TUPLA EM LISTA
(n1,*n2, n3) = nomes # O ASTERISCO SUBSTITUI OS MEMBROS DELE PELOS QUE SOBRARAM NA TUPLA EM FORMA DE LISTA
print (n1)
print (n2)
print (n3)