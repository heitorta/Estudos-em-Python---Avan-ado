#Primeiramente, pra resolver o problema, utilizarei as anotações a seguir que foram dadas, a chave a ser descriptografada é:
# "NBE;JATQAYZZSRQ;VUYOO;SO;Y;XYUC;SR;NBE;JYAC;EYOSEA;NBYR;NBYN;SO;MGON;MGON;NSUN;JUYISRQ;UTU"
#A mensagem está em inglês;
#O caracterer ";" representa espaço;
#Letras iguais representam o mesmo símbolo;
#Z = M;
#O = S;
#Y = A;
#S = I;
#U = L;
#E = E.
#Primeiro, separo a string criptografada e defino uma variável que vai me permitir trocar todos os caracteres nas listas trocar_caracteres.
a_string = 'NBE;JATQAYZZSRQ;VUYOO;SO;Y;XYUC;SR;NBE;JYAC;EYOSEA;NBYR;NBYN;SO;MGON;MGON;NSUN;JUYISRQ;UTU'
trocar_caracteres = [';']
trocar_caracteres2 = ['Z']
trocar_caracteres3 = ['O']
trocar_caracteres4 = ['Y']
trocar_caracteres5 = ['S']
trocar_caracteres6 = ['U']
trocar_caracteres7 = ['E']
#Agora, uso a função zip() pra "zippar" as listas que criei anteriormente.
zipped_caracteres = zip(trocar_caracteres, trocar_caracteres2, trocar_caracteres3, trocar_caracteres4, trocar_caracteres5, trocar_caracteres6, trocar_caracteres7)
#Com a função list(), torno o zip() em uma lista que contém todos iteráveis que utilizarei pra descriptografar.
list_caracteres = list(zipped_caracteres)
#Agora, com todos os caracteres a serem trocados definidos, irei apenas rodar um loop for.
def Conversao()
    for character in list_caracteres:
        a_string = a_string.replace(character,' ')
print(a_string)





