# VARIAVEL GLOBAL
x = "incrivel"

# CRIAR A FUNÇAO + VARIAVEL LOCAL
def myFunc():
    x = "fantastico"
    global z 
    z = "Bem vindo ao curso!"
    print ("Python é "+ x)
    
    
# CHAMAR A FUNÇAO
myFunc()
print ("=================================================")
print ("Voce é "+ x)
print(z)