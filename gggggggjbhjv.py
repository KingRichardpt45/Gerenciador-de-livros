class Stack_Dupla:
    
    def __init__(self):
        
        self.__Fila = [[],[]]
        
    def Adicionar(self,valor,Prioridade=0):
        
        self.__Fila[Prioridade] = self.__Fila[Prioridade] + [valor]
        
    def AlterarPara_Cima(self):
        
        if self.Tamanho(1)>0:
            self.__Fila[0] = self.__Fila[0] + [self.__Fila[1][0]]
            self.__Fila[1] = self.__Fila[1][1:]
            
    def AlterarPara_Baixo(self):
        
        if self.Tamanho(0)>0:
            self.__Fila[1] = self.__Fila[1] + [self.__Fila[0][0]]
            self.__Fila[0] = self.__Fila[0][1:]    
        
    def Remover_Traz(self,Prioridade=None):
        
        t0 = self.Tamanho(0)
        t1 = self.Tamanho(1)
        
        if Prioridade==0 and t0>0:
            self.__Fila[0] = self.__Fila[0][:-1]
        elif Prioridade==1 and t1>0:
            self.__Fila[1] = self.__Fila[1][:-1]
        else:
            if t1>0:
                self.__Fila[1] = self.__Fila[1][:-1]
            elif t0>0:
                self.__Fila[0] = self.__Fila[0][:-1]
            else:
                return None
            
    def Remover_Frente(self,Prioridade=None):
        
        t0 = self.Tamanho(0)
        t1 = self.Tamanho(1)
        
        if Prioridade==0 and t0>0:
            self.__Fila[0] = self.__Fila[0][1:]
        elif Prioridade==1 and t1>0:
            self.__Fila[1] = self.__Fila[1][1:]
        else:
            if t0==0 and t1>0:
                self.__Fila[1] = self.__Fila[1][1:]
            elif t0>0:
                self.__Fila[0] = self.__Fila[0][1:]
            else:
                return None      
              
    def Primeiro(self,Prioridade=None):
        
        t0 = self.Tamanho(0)
        t1 = self.Tamanho(1)
        
        if Prioridade==0 and t0>0:
            return self.__Fila[0][0] 
        elif Prioridade==1 and t1>0:
            return self.__Fila[1][0]
        else:
            if t0==0 and t1>0:
                return self.__Fila[1][0]
            elif t0>0:
                return self.__Fila[0][0]
            else:
                return None
        
    def Tamanho(self,Prioridade=None):
        
        if Prioridade==0:
            return len(self.__Fila[0]) 
        elif Prioridade==1:
            return len(self.__Fila[1])
        else:
            return len(self.__Fila[0]) + len(self.__Fila[1]) 
        
              
    def g(self):
            return self.__Fila   
                    
class Stack:
    
    def __init__(self):
        
        self.__Stack = []
        
    def Adicionar(self,valor):
        
        self.__Stack = [valor] + self.__Stack
        
    def Remover(self):
        
        if self.Tamanho() > 0:
            self.__Stack = self.__Stack[1:]
        else:
            return False
                   
    def Primeiro(self):
        
        if self.Tamanho() > 0:       
            return self.__Stack[0]
        else:
            return None
    
    def Segundo(self):
        
        if self.Tamanho() > 1:       
            return self.__Stack[1]
        else:
            return None    
    
    def Ultimo(self):
        
        if self.Tamanho() > 0:       
            return self.__Stack[-1]
        else:
            return None
    
    def Tamanho(self):
        
        return len(self.__Stack)
    
    def g(self):
