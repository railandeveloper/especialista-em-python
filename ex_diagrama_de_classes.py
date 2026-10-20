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
         return  self.tamanho_lado * 4
         
        
    def area(self):
        return self.tamanho_lado * self.tamanho_lado
    
class  Triangulo(Poligono):
    def __init__(self, tamanho_lado, tamanho_base):
        self.tamanho_lado = tamanho_lado
        self.tamanho_base = tamanho_base
       
    
    def perimetro(self):
        return (self.tamanho_lado * 2) + self.tamanho_base
        
    
    def area(self):
        return (self.tamanho_base * self.tamanho_lado) / 2                    

  
quadrado_1 = Quadrado(12) 
perimetro_quadrado = quadrado_1.perimetro()
area_quadrado = quadrado_1.area()   
print(f'perimetro quadrado: {perimetro_quadrado}')
print(f'area quadrado: {area_quadrado}')     

trangulo_1 = Triangulo(8, 10)
perimetro_triangulo = trangulo_1.perimetro()
area_triangulo = trangulo_1.area()  
print(f'perimetro triangulo: {perimetro_triangulo}')
print(f'area triangulo: {area_triangulo}')      