from Consola import Consola
from TV import TV
from Scooter import Scooter
from Bicicleta import Bicicleta
from Tecnologia import Tecnologia

listconsola = []
listTV = []
listscooter = []
listbici = []

def validar(text,h):
    while True:
            if h =="int":  
                z = int(input(f"{text}"))
                return z
                
            elif h =="float":
                z = float(input(f"{text}"))
                return z
            else:    
              print("Debe ser un valor numerico")
    
def regisconsola():
    voltaje = validar("Ingrese voltaje: ", "int")
    precio = validar("Ingrese precio: ", "float")
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    nomconsola = input("Ingrese nombre de consola: ")
    verconsola = input("¿La consola esta en su versión lite?(y/n): ")
    Consola(voltaje, precio, eficiencia, marca, nomconsola, verconsola)
    listconsola.extend([voltaje, precio, eficiencia, marca, nomconsola, verconsola])

def cotizarconsola():
    precio = validar("Ingrese el precio que busca: ", "float")
    eficiencia = input("Ingrese la eficiencia que busca: ")
    version = input("¿Version Lite?(y/n): ")
    consola = Consola(None, precio, eficiencia, None, None, version)
    consola.calculardctolite()

def registv():
    voltaje = validar("Ingrese voltaje: ", "int")
    precio = validar("Ingrese precio: ", "float")
    eficiencia = input("Ingrese eficiencia: ")
    marca = input("Ingrese marca: ")
    tamano = validar("Ingrese tamaño de TV: ", "float")
    tv = TV(voltaje, precio, eficiencia, marca, tamano)
    tv.calculardcto()
    listTV.extend([voltaje, precio, eficiencia, marca, tamano])

def cotizartv():
    precio = validar("Ingrese el precio de lo que se busca: ", "float")
    eficiencia = input("Ingrese la eficiencia que busca: ")
    tv = TV(None, precio, eficiencia, None,None)
    tv.valortotaldcto()
    return tv

def regisscooter():
    voltaje = validar("Ingrese Voltaje: ", "int")
    precio = validar("Ingrese Precio: ", "int")
    eficiencia = input("Ingrese Eficiencia: ")
    marca = input("Ingrese Marca: ")
    aro = validar("Ingrese Aro: ", "float") 
    velocidad = validar("Ingrese Velocidad: ", "float")
    peso = validar("Ingrese Peso: ", "float")
    Scooter(voltaje, precio, eficiencia, marca, aro, velocidad, peso)
    listscooter.extend([voltaje, precio, eficiencia, marca, aro, velocidad, peso])

def cotizarscooter():
    precio = validar("Ingrese el Precio que busca: ", "float")
    eficiencia = input("Ingrese la Eficiencia que busca: ")
    scooter = Scooter(None, precio, eficiencia, None, None, None, None)
    scooter.valortotaldcto()
    return scooter

def regisbici():
    aro = validar("Ingrese Aro: ", "float")
    peso = validar("Ingrese Peso: ", "float")
    precio = validar("Ingrese Precio: ", "int")
    marca = input("Ingrese Marca: ")
    Bicicleta(aro, peso, precio, marca)
    listbici.extend([aro, peso, precio, marca])    

def cotizarbici():
    pass

while True:
    print("Bienvenido al Menu de productos")
    print("1.- Registrar producto")
    print("2.- Cotizar producto")
    print("3.- Listar productos")
    opcionmenu = input("Seleccione una opcion: ")
    if opcionmenu == "1":
        print("Tipo de producto: ")
        print("1.- Consola")
        print("2.- TV")
        print("3.- Scooter")
        print("4.- Bicicleta")
        opciona = input("Seleccione una opción: ")
        if opciona == "1":
            regisconsola()

        elif opciona == "2":
            registv()

        elif opciona == "3":
            regisscooter()

        elif opciona == "4":
            regisbici()

        else:
            print("Seleccione una opción valida.")       

    elif opcionmenu == "2":
        print("¿Que producto desea cotizar de los que estan en la lista?: ")
        print("1.- Consola")
        print("2.- TV")
        print("3.- Scooter")
        print("4.- Bicicleta")
        opcionb = input("Seleccione una opción de la lista: ")
        if opcionb == "1":
            cotizarconsola()

        elif opcionb == "2":
            cotizartv()

        elif opcionb == "3":
            cotizarscooter()

        elif opcionb == "4":
            cotizarbici()

        else:
            print("Error con opción indicada o producto no encontrado.")    

    elif opcionmenu == "3":
        print("1.- Consola")
        print("2.- TV")
        print("3.- Scooter")
        print("4.- Bicicleta")
        opcionc = input("Seleccione el tipo de producto que desea ver: ")
        if opcionc == "1":
            print(listconsola)

        elif opcionc == "2":
            print(listTV)  

        elif opcionc == "3":
            print(listscooter)

        elif opcionc == "4":
            print(listbici)

        else:
            print("Seleccione una opción valida.")              

    else:
        print("Seleccione una opción valida.")                    



