from Tecnologia import Tecnologia


class Consola(Tecnologia):
    
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,nomConsola:str,version:str):
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__nomConsola = nomConsola
        self.__version = version
        
    def get_nomConsola(self):
        return self.__nomConsola
    
    def get_version(self):
        return self.__version
    
    
    def set_nomConsola(self,nomConsola):
        self.__nomConsola = nomConsola
        
    def set_version(self,version):
        self.__version = version
        
        
    def calculardctolite(self):
        
        if self.__version=="y":
            descuentover = self.get_precio() * 0.05
            costoDescuento = self.get_precio()- descuentover    
            costo_total =  costoDescuento - super().calculardcto()
            print(f'El costo total es: ${costo_total}')
        
        elif self.__version=="n":
            descuento = self.get_precio() - super().calculardcto()
            print(f'El costo total es: {descuento}')

        else:
            print("Valor no valido")    
          
    def impcaracter(self):
        return f'\n Consola: {super().__str__()} \n Nombre consola:{self.__nomConsola} \n Version:{self.__version}'                