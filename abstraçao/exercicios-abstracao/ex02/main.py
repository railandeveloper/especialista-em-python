from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
    
aluno_1 = Aluno('railan', 28, 'ads', 'fundão') 
aluno_1.fazer_aniversario() 
aluno_1.fazer_matricula()
aluno_1.exibir_dados()

profesor_1 = Professor('denis', 42, 'matematica', 'mestrado')
profesor_1.fazer_aniversario()
profesor_1.exibir_dados()
profesor_1.dar_aula()

funcionario_1 = Funcionario('neymar', 35, 'repositor', 'almoxarifado')
funcionario_1.fazer_aniversario()
funcionario_1.exibir_dados()
funcionario_1.bater_ponto()
                                  