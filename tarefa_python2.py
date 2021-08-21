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

 

class Criptografia:
    global string1
    string1 = input('Insira a string a ser descriptografada: ')
    def __init__(self, string):
        self.string = string
    def Descriptografar_1(self):   
        global string1
        string1 = string1
        replaced_string = [';']
        for character in replaced_string:
            string1 = string1.replace(character, ' ')
            print(string1)
    def Descriptografar_2(self):
        global string2
        string2 = string1
        replaced_string2 = ['Z']
        for character in replaced_string2:
            string2 = string1.replace(character, 'M')
            print(string2)
    def Descriptografar_3(self):
        global string3 
        string3 = string2
        replaced_string3 = ['O']
        for character in replaced_string3:
            string3 = string2.replace(character, 'S')
            print(string3)
    def Descriptografar_4(self):
        global string4 
        string4 = string3
        replaced_string4 = ['Y']
        for character in replaced_string4:
            string4 = string3.replace(character, 'A')
            print(string4)
    def Descriptografar_5(self):
        global string5
        string5=string4
        replaced_string5 = ['S']
        for character in replaced_string5:
            string5=string4.replace(character, 'I')
            print(string5)
    def Descriptografar_6(self):
        global string6
        string6 = string5
        replaced_string6 = ['U']
        for character in replaced_string6:
            string6=string5.replace(character, 'L')
            print(string6)
    def Descriptografar_7(self):
        global string7
        string7 = string6
        replaced_string7 = ['E']
        for character in replaced_string7:
            string7=string6.replace(character, 'E')
    def Descriptografar_8(self):
        global string8
        string8=string7
        replaced_string8 = ['*']
        for character in replaced_string8:
            string8=string7.replace(character, 'AA')
            print(string8)



inicio  = Criptografia(input('Clique enter para iniciar o programa.'))
print(inicio.Descriptografar_1())
print(inicio.Descriptografar_2())
print(inicio.Descriptografar_3())
print(inicio.Descriptografar_4())
print(inicio.Descriptografar_5())
print(inicio.Descriptografar_6())
print(inicio.Descriptografar_7())
print(inicio.Descriptografar_8())





