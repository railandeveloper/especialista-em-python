'''crie a classe churrasco, onde seja possivel informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa'''

class Churrasco:
    def __init__(self,titulo, qtd_pessoas):
        self.titulo = titulo
        self.qtd_pessoas = qtd_pessoas
    
    
    def analisar(self):
        consumo_padrao = 0.400
        precokg = 82.40    
        kgs_a_serem_comprados = consumo_padrao * self.qtd_pessoas
        custo_total = kgs_a_serem_comprados * precokg
        custo_por_pessoa = custo_total / self.qtd_pessoas
        print(f'Analisando {self.titulo} com {self.qtd_pessoas} convidados') 
        print(f'recomendo comprar {kgs_a_serem_comprados}kg de carne')   
        print(f'o custo total sera de R${custo_total:.2f}')
        print(f'cada pessoa pagara R${custo_por_pessoa}')
        
churras_1 = Churrasco('churras dos brothers', 15)
churras_1.analisar()        