set1= {"Carlos", "Jonas", "Marcos", 2, 3}
set2= {1,2,3}

#JUNTAS DOIS SET (IMPORTANTE:ELES APAGA OS ITENS DUPICADOS)
#set1.update(set2)
#print (set1)

#set3 = set1.union(set2)
#print(set3)

#MANTEM SEMOMENTE OS REPETIDOS NAS 2 COLEÇOES
#set1.intersection_update(set2)
#set3 = set1.intersection(set2) #CRIA NOVA VARIAVEL SOMENTO OS DUPLICADOS
#print (set1)
#print (set2)
#print (set3)

#MANTEM TODOS MENOS OS REPETIDOS
#set1.symmetric_difference_update(set2)#Altera a "set1" para todos menos os repetidos
#print(set1)

set4 = set1.symmetric_difference(set2)# CRIA NOVA VARIAVEL COM TODAS MENOS OS REPETIDOS
print(set4)

