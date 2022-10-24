class Bicicleta():
    
    def __init__(self,aro:float,peso:float,precio:float,marca:str):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca
        
    def get_aro(self):
        return self.__aro
    
    def get_peso(self):
        return self.__peso
    
    def get_precio(self):
        return self.__precio
    
    def get_marca(self):
        return self.__marca
    
    
    def set_aro(self,aro):
        self.__aro = aro
        
    def set_peso(self,peso):
        self.__peso = peso
        
    def set_precio(self,precio):
        self.__precio = precio
        
    def set_marca(self,marca):
        self.__marca
        
    def impcaracter(self):
        return f'\n Bicicleta: \n Aro: {self.__aro} \n Peso: {self.__peso} \n Precio: {self.__precio} \n Marca: {self.__marca}'