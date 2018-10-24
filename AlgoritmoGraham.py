import pygame # necesito instalarlo: desde una linea de comandos -> pip install pygame
import time
import math

class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)

class Poligono:

    def __init__(self):
        self.lista=[]
    def anadir(self,p):
        self.lista.append(p)
    def buscar(self,p):
        return self.lista.index(p)

    def __repr__(self):
        l=""
        for i in self.lista:
            l+=str(i)
        return l

    def puntoInicial(self):
        i=10000
        for j in self.lista:
            if j.y<i:
                    menor = j
                    i=menor.y
                    return menor


class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def shift(self,x,y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Punto(",str(self.x),",", str(self.y), ")"])


def Area2 ( a,b,c):
    return (b.x - a.x) *(c.y - a.y) - (c.x - a.x) * (b.y - a.y)



def AreaSign(a,b,c):
    area2= (b.x - a.x) *(c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    if(area2>= 0.5 or area2>= 0.0):
        return 1
    elif(area2< -0.5):
        return -1
    else:
        return 0


def Left(a,b,c):
    return AreaSign(a,b,c)>0

def CalculoAngulo(a,b):
    division= a.x+b.x

def CalculoModulo(a,b):
    return math.sqrt(((b.x-a.x)**2)+((b.y-a.y)**2))

def EleccionPuntoExterior(arr):
    x=0
    y=10
    punto = Punto(0.0,0.0)
    candidatos = []
    for i in range(len(arr)):
        if(arr[i].y<y):
            x=arr[i].x
            y=arr[i].y
    for j in range(len(arr)):
        if(arr[j].y==y):
            candidatos.append(arr[j])
    if(len(arr)>0):
        for k in range(len(candidatos)):
                if(candidatos[k].x>x):
                    x=candidatos[k].x
    punto.x=x
    punto.y=y
    return punto
def CalculoAnguloMasCercano(a):
    anguloInicial=100
    elementoMasCercanot=100
    angulos = []
    puntos = []
    angulosOrdenados = []
    indices = []
    tamanyo=len(arr)
    i=0
    j=0
    while j <tamanyo:
        print(i," ",tamanyo, " inicial x: ",a.x, " inicial y: ",a.y, " arr[i].x: ",arr[i].x, " arr[i].y: ",arr[i].y)
        print("Mi vector vale: ",puntos)
        if(a.x==arr[i].x and a.y==arr[i].y):
            arr.remove(arr[i])
            j=j+1
        else:
            angulo=math.atan2(arr[i].y-a.y,arr[i].x-a.x)
            if(angulo<0):
                angulo=angulo*(-1)
            angulos.append(angulo)
            angulosOrdenados.append(angulo)
            puntos.append(arr[i])
            i=i+1
            j=j+1
    #print(len(arr))
    angulosOrdenados.sort()
    print("El array vale:                ",puntos)
    print("Los angulos al principio son: ",angulos)
    indices=OrdenaVectores(angulos,angulosOrdenados,puntos)
    print("El vector ordenado es:        ",indices)
    print("Los angulos ordenados son:    ", angulosOrdenados)
    print("El vector ordenado es:        ",indices)


    return indices
#EM ESTE METODO COMO HAGO PARA QUE NO SE REPITAN LOS VALORES !!! SI NO TENGO EN CUENTA EN ESTO SI SON DISTINTOS TODO VA BIEN
def OrdenaVectores(angulos,angulosOrdenados,puntos):
    indices = []
    j = 0
    i = 0
    print()
    print(angulosOrdenados)
    print(angulos)
    while j<len(puntos):
        if(angulosOrdenados[j]==angulos[i]):
            print("El angulo ordenado en la posicion i ",i, " tiene un valor de ",angulosOrdenados[j])
            print("El angulo en la posicion j ",j," tiene un valor de ",angulos[i])
            indices.insert(j,puntos[i])
            angulos[i]=999
            print(indices)
            j=j+1
            i=0
        else:
            i=i+1
    return indices

def CalculoAngulo(a,b):
    math.atan2(b.y-a.y,b.x-a.x)
    return

def CrearMalla(a):
    i=0
    j=2

    while(i<len(indiceMasCercano)):
        print(pila)
        print(indiceMasCercano)
        print("Hola soy el left y valgo?: ",Left(pila[j-2],pila[j-1],indiceMasCercano[i]),"Teniendo en cuenta que a vale: ", pila[j-2],"El de la pila vale: ",pila[j-1],"y el array vale: ",indiceMasCercano[i])
        if(len(pila)<2):
            pila.append(indiceMasCercano[i])
            j=j+1
            i=i+1
        elif(Left(pila[j-2],pila[j-1],indiceMasCercano[i])==True):
            pila.append(indiceMasCercano[i])
            print("Se anyade en la pila e i vale: ",i)
            j=j+1
            i=i+1
        else:
            pila.pop()
            j=j-1
            print("Se extrae en la pila")

"""Con estos puntos funciona"""
"""p1 = Punto(4.0,3.0)
p2 = Punto(2.0,1.0)
p3 = Punto(1.0,5.0)
p4 = Punto(5.0,4.0)
p5 = Punto(8.0, 6.0)
p6 = Punto(0.0,3.0)
p7 = Punto(7.0,2.0)
p8 = Punto(8.0,5.0)
arr = [p1,p2,p3,p4,p5,p6,p7,p8]
"""
"""
p1 = Punto(5.0,2.0)
p2 = Punto(2.0,1.0)
p3 = Punto(0.0,3.0)
p4 = Punto(4.0,4.0)
p5 = Punto(3.0,7.0)
p6 = Punto(7.0,6.0)
p7 = Punto(10.0,4.0)
p8 = Punto(7.0,2.0)
p9 = Punto(10.0,3.0)
p10 = Punto(8.0,3.0)
p11 = Punto(9.0,1.0)
p12 = Punto(8.0,0.0)
p13 = Punto(10.0,2.0)
arr = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
"""
p1 = Punto (1, 2)
p2 = Punto (5, 2)
p3 = Punto (2, 3)
p4 = Punto (2, 4)
p5 = Punto (2, 1)
p6 = Punto (3, 2)
p7 = Punto (4, 1)
p8 = Punto (1, 3)
poligono=Poligono()
z = Punto(0.0,0.0)
arr = [p1,p2,p3,p4,p5,p6,p7,p8]
pila = []
poligono_completo=[]

z= EleccionPuntoExterior(arr)
poligono.anadir(z)
pila.append(poligono.lista[0])
print("El punto elegido es: ",z)
print(arr)
indiceMasCercano=CalculoAnguloMasCercano(z)
print("Los indices son: ",indiceMasCercano)
poligono.anadir(indiceMasCercano[0])
pila.append(poligono.lista[1])
indiceMasCercano.pop(0)
CrearMalla(z)
for i in pila:
    i= [i.x*100,i.y*100]
    poligono_completo.append(i)
print(poligono_completo)
size = [1500, 1500]
screen = pygame.display.set_mode(size)

GREEN = (  0, 255,   0)
pygame.draw.lines(screen, GREEN, True, poligono_completo,1)
pygame.display.flip()
time.sleep(15.5) #necesario para no cerrar la pantalla inmediatamente
pygame.quit()
print("El poligono esta formado por: ",poligono)




#print("se borarria el elemento",arr.pop(arr.index(c)))
#punto2=CalculoPuntoMasCercano(arr)
#Si buscara el menor punto sería así
#(poligono.puntoInicial())
#Si quisiera saber la posicion dentro del poligono haria esto
#posicionPoligono=poligono.buscar(c)
#print("El elemento esta en la posicion ",posicionPoligono)
#print("El elemento del array mas cercano al punto intermedio es: ",CalculoPuntoMasCercano(arr))
"""LOS ANGULOS SE COGEN EN FUNCIÓN DEL PRIMERO ENTONCES LAS LETRAS VIENEN DADAS POR LA CERCANIA A LOS PUNTOS
    Entonces para ello debo crear una lista ejn función de los angulos sobre eso ordenarlo y ya despues que se haga lo que se esta haciendo ahora."""
"""b = Punto(2.0,1.0)
d = Punto(1.0,5.0)
a = Punto(4.0,3.0)
e = Punto(5.0,4.0)
f = Punto(8.0, 6.0)
c = Punto(0.0,3.0)
g = Punto(7.0,2.0)"""
