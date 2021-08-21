#Calculadora de ano bissexto
#Inicialmente, definamos o que é um ano bissexto:
#Um ano bissexto é qualquer ano que possui resto da divisão por 4 = 0
#Ou para alguns outros anos múltiplos de 100, devem ser múltiplos de 400 também.
def calculadora():
    global ano_inserido
    global ano_proximo
    
    #Transformo a variável ano_inserido em global 
    #apenas por rigor, não é necessário.
    ano_inserido = int(input('Insira o ano: '))
    n = ano_inserido % 4
    n1 = n // 4 
    n2 = n1 + 4
    if ano_inserido % 4 == 0 or ano_inserido % 100 == 0 and ano_inserido % 400 == 0:
        #Agora, com um if/else, utilizo operadores
        #lógicos (or, and) aplicando a regra do ano bissexto.
        #os operadores or e and funcionam dentro do if e 
        #funcionam como uma cascata de if's
        print(f'{ano_inserido} é ano bissexto!')
    else:
    #O operador else funciona como um ''if''
    #a diferença é que ele retorna tudo o que não estiver
    #dentre os ifs anteriores.
        print(f'{ano_inserido} não é bissexto')

calculadora()
