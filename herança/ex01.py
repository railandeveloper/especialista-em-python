class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade +=1    
        
    def exibir_dados(self):
        print(f'Nome: {self.nome} idade:{self.idade}')
            
        

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
        
        
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
        
    def dar_aula(self):
        print(f'professor: {self.nome} iniciou a aula')
 
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f'{self.nome} acabou de bater o ponto')
    
    
aluno_1 = Aluno('railan', 28, 'ads', 'fundão') 
aluno_1.fazer_aniversario() 
aluno_1.fazer_matricula()
aluno_1.exibir_dados()

profesor_1 = Professor('denis', 42, 'matematica', 'mestrado')
profesor_1.exibir_dados()
profesor_1.dar_aula()

funcionario_1 = Funcionario('neymar', 35, 'repositor', 'almoxarifado')
funcionario_1.exibir_dados()
funcionario_1.bater_ponto()
                                  