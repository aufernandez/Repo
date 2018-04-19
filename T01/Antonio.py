##
# coding: utf-8

# In[16]:


from CONSTANTES import PERSONAS, ATRACCIONES
from collections import deque
from datetime import date,datetime

class Persona:
    def __init__(self, dinero = 0):
        self.dinero = dinero
class Parque:
    def __init__(self,atracciones):  #el input va a ser una lista con las 5 atracciones más caras
    
        self.atracciones = atracciones#FALTA CREAR LA CLASE "Atraccion"
#print(ATRACCIONES)

#class Atraccion:
#    def __init__(self,nombre,capacidad,entrada,costo,tiempo): #El input son todos los datos de una ATRACCION
#        self.nombre=nombre
#        self.capacidad=capacidad
#        self.entrada=entrada               #costo_entrada
#        self.costo=costo                   #costo_atraccion (lo que cuesta comprarla)
#        self.tiempo=tiempo                 #minutos_por_vuelta
#        
#        self.cola=deque()                  #los que están esperando para entrar
#        self.usuarios=[]                   #los que están adentro de la atracción
#        self.recaudacion=0                 #***lo recaudado hasta el momento, en algún momento esto se traspasa a Antonio
#        self.contador_clientes=0           #***lleva la cuenta de todos los que han ENTRADO, no sé si voy a usar esto jaja
#        self.reloj=self.tiempo             #cuenta regresiva, parte siendo los minutos_por_vuelta. A medida que avanza la 
#                                           #simulación va bajando hasta llegar a 0, donde se sube una nueva tanda de 
#                                           #clientes y vuelve a ser self.tiempo
#        self.disponible=True               #***Esto va a ser False cuando esté siendo usada o cuando haya fallado y esté
#                                           #cerrada por 1 hora. Puede que sea innecesaria


# In[21]:


#lista_objetos_atracciones = []
#
#for key in ATRACCIONES.keys():
#    Objeto = Atraccion(key, ATRACCIONES[key][0], ATRACCIONES[key][1], ATRACCIONES[key][2], ATRACCIONES[key][3])
#    
#    lista_objetos_atracciones.append(Objeto)
#    
#for i in lista_objetos_atracciones:
#    print(i.nombre)
#

# In[14]:


#dic ={0:'abc',1:'bcd',2:'cde'}
#for k in dic.keys():
#    a = dic[k][k]
#    print (a)


# In[9]:



#atracciones_parque = [] ###HAY QUE CAMBIARLO, la lista es un atributo del objeto parque
class Antonio(Persona):
    def __init__(self, dinero = 100000):
        self.dinero = dinero   ###dinero dinero dinero aprende algo dinero
    def comprar_atraccion(self):   ##asumiendo una lista 'atracciones' con objetos de las del archivo ordenadas de mayor a menor
        self.dinero = self.dinero/2
        atracciones_parque.append(atracciones.pop())
    def duplicar_precios(self, atracciones):
        for atraccion in atracciones_parque:
            atraccion.entrada = atraccion.entrada*2


# In[10]:


### COMO SERIA EL FUNCIONAMIENTO:
##PlaceHolder = Parque([]) #placeholder nombre
##for i in range(1,4):
##    print(i)
##    PlaceHolder.atracciones.append(.pop())   ###CAMBIAR LA LISTA Y EL NOMBRE
    

