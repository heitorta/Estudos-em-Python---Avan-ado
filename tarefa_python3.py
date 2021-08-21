# Para a resolução do problema, primeiramente fixarei em
# um comentário a chave a ser descriptografada
# "NBE;JATQAYZZSRQ;VUYOO;SO;Y;XYUC;SR;NBE;JYAC;EYOSEA;NBYR;NBYN;SO;MGON;MGON;NSUN;JUYISRQ;UTU"
# Assim, começo definindo a classe Criptografia para assim criar minhas funções


class Criptografia:
    global mensagem
    mensagem = input('Insira a mensagem a ser descriptografada: ' )
    mensagem = mensagem.lower()
    
    def __init__(self,string):
        self.string = string
        pass
# Usando o def, crio a função que irá rodar toda e qualquer chave que eu quiser
    def descriptografar_1(self):
        chave_descript = ""
        # O dicionário chave funciona em pares de key:values, ou seja, 
        # assim posso relacionar o dicionário às letras
        # que serão trocadas no programa.
        chave = {';': ' ', 'a': 'r', 'b': 'h', 'c': 'k', 'e': 'e', 'g': 'u', 'i': 'y', 'j': 'p', 'm': 'j', 'n': 't', 
                 'o': 's', 'q': 'g', 'r': 'n', 's': 'i', 't': 'o', 'u': 'l', 'v': 'c', 'x': 'w', 'y': 'a', 'z': 'm'}
        # Com um loop for, rodo a chave somando as strings.
        for letra in mensagem:
            chave_descript = chave_descript + chave[letra]
        print(chave_descript.capitalize())
# Agora só crio a variável inicio, invocando a classe Criptografia e
# executo a função Descriptografar_1() em seguida.     
inicio=Criptografia(input('Clique enter para rodar o programa'))
inicio.descriptografar_1()
# O dever foi realizado em conjunto com o Marcos Paulo de Oliveira,
# que também está na turma de Python, por isso nossos códigos estão
# tão semelhantes :)