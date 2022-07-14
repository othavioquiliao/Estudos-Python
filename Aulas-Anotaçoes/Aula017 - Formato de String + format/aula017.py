quantidade = 3
item = "bolo de morango"
valor = 23.50

# Aqui tu usar FORMAT QUE SEGUE UMA ORDEM DETERMINADA AUTOMATICAMENTE
meuPedido = "Eu quero {} fatias de {} no valor de {}!"
print (meuPedido.format(quantidade, item, valor))

# AQUI TU MANIPULA A ORDEM USANDO OS INDICES COM O COMANDO FORMAT
meuPedido2 = "Paulo, pega {0} fatias do {2}, se possivel no maximo {1}!"
print (meuPedido2.format(quantidade, valor, item)) #Aqui dita a ordem
