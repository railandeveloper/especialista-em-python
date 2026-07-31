'''crie a classe produto, onde podemos cadastrar nome e o preco. crie tambem um metodo que mostre uma etiqueta de preco do produto'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        print(f'Produto {self.nome.lower()}| Preco R${self.preco}')    
        
p1 = Produto('ps5', 3500)    
p1.etiqueta()    