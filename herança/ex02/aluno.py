from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma  
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f'Curso: {self.curso}, Turma: {self.turma}')
        
    def fazer_matricula(self):
        print(f'O aluno {self.nome} se matriculou no curso de {self.curso}')