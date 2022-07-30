'''CALORIMETRIA
Una muestra de 600 gramos de agua 0en estado liquido se calienta de 15ºC a 90ºC
determine la canridad de calor que se debe absorber Q=C(T1-T2)
Donde:
Q=calor
C=capacidad calorifica (masa*calor especifico)
T1=temperatura inicial
T2=temepratura final '''
#Crear la clase
class Calor:
    def __init__(self):
        self.temperatura1 = int(input('ingresar la temperatura 1:'))
        self. temperatura2 = int(input('ingresar la temperatura 2:'))
        self.masa = int(input('ingresar la masa (en gramos):'))
        self.S= float(input('ingresar el calor especifico (J/g*ºC)'))
        self.Diferencia_de_T=( (self.temperatura2)-(self.temperatura1))
        self.capacidad_calorifica=((self.masa)*(self.S))
#Realizar los metodos
          
    def calor_absorbido (self):
        self.calora=((self.Diferencia_de_T)* (self.capacidad_calorifica))
        print('El calor absorbido es:', round(self.calora,2),'Joules')

    def mostrar_datos (self):
         print("La capacidad calorifica es:",self.capacidad_calorifica)
         print("La diferencia de calor es:",self.Diferencia_de_T)
     
    def imprimir(self):
        return print("Fin del programa")
    
#Crear el objeto
ca = Calor ()
#Intanciar la clase
print()
print('Los datos son:')
ca.mostrar_datos ()
print()
print("Los valores son:")
ca.calor_absorbido ()
ca.imprimir ()
