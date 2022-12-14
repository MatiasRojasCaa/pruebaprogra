from Tecnologia import Tecnologia


class Scooter(Tecnologia):
    
    def __init__(self,voltaje:str,precio:float,eficiencia:str,marca:str,aro:float,velocidad:int,peso:float):
        Tecnologia.__init__(self,voltaje,precio,eficiencia,marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        
    def get_aro(self):
        return self.__aro
    
    def get_velocidad(self):
        return self.__velocidad
    
    def get_peso(self):
        return self.__peso
    
    
    def set_aro(self,aro):
        self.__aro = aro
        
    def set_velocidad(self,velocidad):
        self.__velocidad = velocidad
        
    def set_peso(self,peso):
        self.__peso = peso
        
    def valortotaldcto(self):
      total = self.get_precio() - super().calculardcto()
      print(f'El valor con descueto es de: {total}')
        
    def impcaracter(self):
        return f'\n Scooter: {super().__str__()} \n Aro: {self.__aro} \n Velocidad: {self.__velocidad} \n Peso: {self.__peso}'

                       