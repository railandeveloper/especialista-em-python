class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade +=1    
        
    def exibir_dados(self):
        print(f'Nome: {self.nome} idade:{self.idade}')