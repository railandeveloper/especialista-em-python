from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
       
            
    @abstractmethod
    def calcular_frete(self):
        pass    


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
        
            
    def calcular_frete(self):
        calculo_frete = self.distancia * self.fator
        print(f' valor do frete fica em R${calculo_frete:.2f}')        
            

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
              
    def calcular_frete(self):
        if self.distancia < 50:
            print('disntacia muito curta, nao e possivel levar de caminhao = Raio minimo de 50km')
        else:
            calculo_frete = self.distancia * self.fator
            print(f'o valor do frete fica em R${calculo_frete:.2f}')
       
    
    
class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50
             
    def calcular_frete(self):
        if self.distancia > 10:
            print('distancia muito longa = Raio maximo de 10km')
        else:
            calculo_frete = self.distancia * self.fator
            print(f'o valor do frete fica em R${calculo_frete:.2f}')        
            

entrega_1 = Drone(8)  
entrega_1.calcular_frete()          