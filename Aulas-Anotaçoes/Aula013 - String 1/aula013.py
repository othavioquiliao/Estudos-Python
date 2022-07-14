#Para acessar uma informaçao no String
e = "Ola mundo !"

# print (e[2])

#----------------------------------------------------------------------------------
# for x in "Othavio":

#    print (x)
#----------------------------------------------------------------------------------
# y = len(e)

# print(y)

#----------------------------------------------------------------------------------
# VERIFICAR SE ALGO ESTA PRESENTE NA VARIAVEL!!
txt = "Seja bem vindo ao curso de Python"

x = "vindo" in txt
print(x)
l = "carlos" in txt
print(l)

#----------------------------------------------------------------------------------
#VERIFICAR SE ESTA PRESENTE NO TXT
if "vindo" in txt:
    print("Sim, 'vindo' esta presente")

#VERIFICAR SE NAO ESTA PRESENTE NO TXT
if "carlos" not in txt:
    print("Nao, 'othavio' nao esta presente")
