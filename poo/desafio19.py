#CRIE a classe livro, que vai simular a passagem de paginas de um livro, considrando tambem, se o usuario chegou ao fim da leitura.

class Livro:
    def __init__(self, nome, qtd_paginas):
        self.nome = nome
        self.qtd_paginas = qtd_paginas
        self.pagina_atual = 1
        if self.pagina_atual == 1:
            print(f'voce acabou de abrir o livro {self.nome}, que tem {self.qtd_paginas} paginas no total. voce esta agora na pagina {self.pagina_atual}' )
    
       
    def avancar_paginas(self, qtd):
        if qtd <= self.qtd_paginas:
            for contador in range(self.pagina_atual+1, self.pagina_atual+qtd+1, 1):
                print(f'pag{contador}')
            self.pagina_atual +=qtd
            if self.pagina_atual == self.qtd_paginas:
                print(f'voce avancou {qtd} paginas e agora esta na pagina {self.pagina_atual} ')  
                print('voce chegou no fim do livro')
            else:
                print(f'voce avancou {qtd} paginas e agora esta na pagina {self.pagina_atual} ')    
      
livro_1 = Livro('mundo python', 20) 
livro_1.avancar_paginas(5) 
livro_1.avancar_paginas(10)  
livro_1.avancar_paginas(4)
livro_1.avancar_paginas(100)