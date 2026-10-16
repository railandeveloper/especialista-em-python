from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self):
        pass
       
    
    @abstractmethod
    def perimetro(self):
        pass
    
    
    @abstractmethod
    def area(self):
        pass    
    

class  Quadrado(Poligono):
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        
        
    
    def perimetro(self):
         calculo_perimetro_quadrado =  self.tamanho_lado * 4
        
    
    def area(self, largura, altura):
        calculo_area_quadrado = largura * altura
    
    
class  Triangulo(Poligono):
    def __init__(self, tamanho_lado, tamanho_base):
        self.tamanho_lado = tamanho_lado
        self.tamanho_base = tamanho_base
       
    
    
    def perimetro(self):
           calculo_perimetro_triangulo = self.tamanho_lado * 2 + self,self.tamanho_base
        
    
    def area(self):
        calculo_area_triangulo= (self.tamanho_base * self.tamanho_lado) / 2                          

  
quadrado_1 = Quadrado(10)         