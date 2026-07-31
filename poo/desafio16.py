'''Desafio 16: Classe Funcionário
crie a classe fucnonario, onde podemos cadastrar nome, setor e cargo, crie tambem um metodo que permite ai funcionario se apresentar'''


class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentar(self):
        print(f'meu nome é {self.nome}, sou do setor de {self.setor} e atuo como {self.cargo}')
        


funcionario1 = Funcionario('railan', 'ti', 'desenvolvedor beck end')      
funcionario1.apresentar()  
        