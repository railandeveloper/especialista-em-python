'''crie a classe gamer, onde podemos cadstrar nome, nick e jogos favoritos de uma pessoa. crie tambem um metodo que permita mostrar a ficha desse gamer '''

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista_favoritos = []
    
    def mostrar_ficha(self):
        print(f'nome:{self.nome}')
        print(f'nick:{self.nick}')
        print('lista de jogos')
        for jogo in self.lista_favoritos:
            print(jogo)
    
    def add_favoritos(self, jogo):
        self.lista_favoritos.append(jogo)    

gamer_1 = Gamer('railan', 'sunn')    
gamer_1.add_favoritos('god of war')  
gamer_1.add_favoritos('mario bros')  
gamer_1.mostrar_ficha()

gamer_2 = Gamer('lucas', 'terror')
gamer_2.add_favoritos('creed')
gamer_2.mostrar_ficha()