"""
Este código ns mostra a função print que mostra uma mensagem no terminal e 
demonstra o conceito de variáveis

print("Hello, World!")
name = input("What's your name?\n")
print(f"Hi,{name}!\nThis is your first python program!")

---------------------------------------------------------------------
este código implementa condicionais
if condição:
    execução
OBS: Note que para que o codigo seja executado a condição deve ser atendida, 
Ex:
n = int(input("Input a number: "))
if n>0:
    print(f"{n} is positive!")
elif n<0:
    print(f"{n} is negative!")
else:
    print(f"{n} is zero")
    
-------------------------------------------------------------------------

Aqui somos intrduzidos o conceito de Arrays(listas),
para definir arrays coloque o valor entre colchetes [],
Ex:

names = ["Harry","Rony", "Hermione"]
print(names)            #Podemos acessar as informações da array por completo ou
print(names[0])         #Podemos acessar um valor específico da array

names.append("Draco")   #Incluimos uma nova informação no array com o atributo .append()
print(names)
names.sort()            #Organizamos a array com o atributo .sort()
print(names)

--------------------------------------------------------------------------

Aqui somos introduzidos ao conceito de conjuntos bem semelhante a arrays
com a diferença que valores repitidos na entrada não saõ duplicados na saida.
os valores de saida estarão organizados em ordem crescente
Ex:

#aqui criamos um conjunto vazio
s = set()

#Agora adicionamos valores ao conjunto
s.add("Harry")                  #.add adiciona elementos ao conjunto, apenas 1 por vez
s.add("Rony")
s.add("Hermyone")
s.add("Draco")
print(s)

s.remove("Draco")               #.remove remove o elemento informado
print(s)

print(f"O conjunto s possui {len(s)} elementos") #len mostra o número de elementos

-----------------------------------------------------------------------------

Aqui somos apresetados ao conceito de loops
Loop For
para cada elemento dentro da array seja numeros ou string faça
    comando

ex:
for i in [0,1,2,3,4]:
    print(i)

se quisermos que ele conte até n numeros

for i in range(6):   #Aqui conta em um intervalo de 6 numeros, contando apartir do 0
    print(i)
    
se quisermos que mostre caracteres em uma string

nome = "Renan"
for i in nome: #aqui ele percorrer cada letra da string
    print(i)
    
---------------------------------------------------------------------------------------

Aqui somos apresentados os conceitos de Dicionários
utilizamos dicionários quando queromos associar uma informação a outra, por exemplo

Harry, Rony, Hermione são da grifinoria
Draco é da sonserina

quero um programa que:
ao verificar o nome do aluno
mostre em qual casa de Hogwarts ele está

#aqui criamos um dicionário utilizando {"palavra Chave":"Valor atribuido a palavra chave"}
hogwarts = {"Harry":"Grifinória", "Rony":"Grifinória", "Hermione":"Grifinória"} 
print(hogwarts["Harry"])

#podemos adicionar novas palavras chaves ao dicionário
hogwarts["Draco"] = "Sonserina"
print(hogwarts["Draco"])

-----------------------------------------------------------------------------------

Aqui somos introduzidos ao conceito de Funcões (def)
E funçoes são uteis para podermos implemetá-lo ao longo do código.

por exemplo: Quero uma função que retorne o uadrado de um número

def quadrado(x):
    return x*x

for i in range(10):
    print(f"O quadrado de {i} é: {quadrado(i)}")
    

podemos também colocar esta função em um arquivo separado
e importá-la para este arquivo

Ex:
criamos o arquivo quadrad.py e colocamos a função nele
        |quadrado.py
        |   def quadrado(x):
        |   return x*x
    
em nosso aquivo atual
hello.py
    from hello import quadrado      #Aqui importamos as funções de quadrado para dentro de hello 

    for i in range(10):
    print(f"O quadrado de {i} é: {quadrado(i)}")
    
e o resultado será o mesmo

-------------------------------------------------------------------------

Aqui somos apreentados ao conceito de classes (class)
que seria um modelo para um tipo de objeto que possue caracteristicas específicas


Estudar classes e decoradores e tratamento de erros(Exeptions)
"""
