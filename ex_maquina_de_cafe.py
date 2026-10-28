#simule uma cafeteira orientada a obejtos

from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self):
        pass
    
    
    def preparar(self):
        print(' --- iniciando o preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f'--- Bebida Pronta ---')
    
    
    def ferver_agua(self):
       print('1. Fervendo agua a 100 graus celsius.')
    
    
    @abstractmethod     
    def misturar(self):
        pass
    
    
    @abstractmethod
    def servir(self):
        pass
    


class Cafe(BebidaQuente):
    def __init__(self):
       pass
   
      
    def misturar(self):
        print('2. Passando agua pressurizada pelo pó de café moido')
    
    
    def servir(self):
        print('3. Servindo em xicara pequena.') 
    


class Cha(BebidaQuente):
    def __init__(self):
       pass
   
    
    def misturar(self):
        print('2. Mergulhando o sache de ervas na agua') 
    
    
    def servir(self):
         print('3. Servindo na caneca de porcelana com limão.')



class Leite(BebidaQuente):
    def __init__(self):
       pass
   
    
    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite')
    
    
    def servir(self):
        print('servindo na caneca grande, ja com cafe')
    


cafe_1 = Cafe()
cafe_1.preparar()



cha_1 = Cha() 
cha_1.preparar()


leite_1 = Leite() 
leite_1.preparar()

               