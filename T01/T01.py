
# coding: utf-8

# In[2]:


from CONSTANTES import PERSONAS, ATRACCIONES
from collections import deque
from datetime import date,datetime
from abc import ABCMeta, abstractmethod


# In[3]:


def birth_to_age(fecha):  #función para obtener la edad a partir de la fecha de nacimiento
    j=fecha
    año = int(j[0]+j[1]+j[2]+j[3])
    mes = int(j[5]+j[6])
    dia = int(j[8]+j[9])
    birth_date = date(año, mes, dia)
    years = date.today().year - birth_date.year
    if (date.today() - birth_date.replace(year=date.today().year)).days >= 0:
        age = years
    else:
        age = years - 1
    return age
#a=birth_to_age('2005-10-16')
#print(a)


# In[12]:

class Persona(metaclass = ABCMeta):
    def __init__(self, dinero = 0):
        self.dinero = dinero
        
        
class Parque:
    def __init__(self,atracciones = []):  #el input va a ser una lista con las 5 atracciones más caras
    
        self.atracciones = atracciones
        
        
class Dueno(Persona):
    def __init__(self, dinero = 100000):
        self.dinero = dinero   ###dinero dinero dinero aprende algo dinero
    def comprar_atraccion(self):   ##asumiendo una lista 'atracciones' con objetos de las del archivo ordenadas de mayor a menor
        self.dinero = self.dinero/2
        atracciones_parque.append(atracciones.pop())
    def duplicar_precios(self, atracciones):
        for atraccion in atracciones_parque:
            atraccion.entrada = atraccion.entrada*2

Antonio= Dueno()
TheLonelyIsland= Parque()
            
            
class Atraccion:
    def __init__(self,nombre,capacidad,entrada,costo,tiempo,dueno): #El input son todos los datos de una ATRACCION
        self.nombre = nombre
        self.capacidad = capacidad
        self.entrada = entrada             #costo_entrada
        self.costo = costo                 #costo_atraccion (lo que cuesta comprarla)
        self.tiempo = tiempo               #minutos_por_vuelta
        self.dueno = dueno
    
        
        self.cola = deque()                #los que están esperando para entrar
        self.usuarios = []                 #los que están adentro de la atracción
        self.recaudacion = 0               #***lo recaudado hasta el momento, en algún momento esto se traspasa a Antonio??
        self.contador_clientes = 0         #***lleva la cuenta de todos los que han ENTRADO, no sé si voy a usar esto jaja
        self.reloj = 0                     #cuenta regresiva, parte en 0 para que la función cuenta_regresiva se ejecute
                                           #cuando parta la simulación (la primera subida ocurre solo si reloj==0.
                                           #A medida que avanza la simulación va bajando hasta llegar a 0, donde se 
                                           #sube una nueva tanda de clientes y vuelve a ser self.tiempo
        
        self.disponible = True             #***Esto va a ser False cuando esté siendo usada o cuando haya fallado y esté
                                           #cerrada por 1 hora. Puede que sea innecesaria
        self.reparacion = 60               # es lo mismo que self.reloj , pero empieza a andar después de que la atracción falla
   
    def aceptar_visitante (self,visitante):   #visitante es una instancia de la clase Visitante. Acá se suma a la cola
        
        self.cola.append(visitante)
        print('{0} se va a la cola de {1}'.format(visitante.nombre,self.nombre)
        #print(self.cola)
        
    def subir_visitantes (self):  #recibe al dueño como argumento, para que se le pague a él la entrada

        for i in range(min(len(self.cola),self.capacidad)):   #Se suben los que quepan, o todos (si es que hay menos que la capacidad)
            #subida
            siguiente = self.cola.popleft()                   #"siguiente" es un Visitante

            #pago:            
            if siguiente.edad <=8:
                pago = self.entrada/2
                
            else:
                pago = self.entrada            
            
            siguiente.dinero = siguiente.dinero - pago   
            self.dueno.dinero = self.dueno.dinero + pago
            self.usuarios.append(siguiente)
            self.contador_clientes = self.contador_clientes + 1
            self.recaudacion +=pago
            if self.contador_clientes == 100:
                self.fallar()                   #PENDIENTE
                break                           #dejamos de subir clientes
        print('{0} recaudó {1} en esta vuelta'.format(self.nombre,self.recaudacion)            
        self.recaudacion == 0
        if len(self.usuarios) > self.capacidad:   #Un paréntesis, para cachar si el programa llegase a fallar
            
            print("El {} está sobre cargado perrito".format(self.nombre))      

    def cuenta_regresiva (self):                  #Esta función dirá cuándo inicia y termina un ciclo de uso o un ciclo
                                                  #de reparación. Se llama cada vez que avanza el reloj de la simulación.
        
        if self.disponible and self.usuarios:    #EN ESTE CASO la atracción está andando y corriendo su tiempo de juego
            self.reloj = self.reloj - 1          #(solo cuando hay gente arriba y está disponible)
       
        if self.disponible and self.reloj == 0:  #la primera condición es para evitar que suban clientes si la máquina está fallada
            for usuario in self.usuarios:        #Cada usuario busca su siguiente atracción (si no hay usuarios, no se itera)
                usuario.elegir_atraccion()  
            self.usuarios=[]                     #vaciamos el juego
            
            #Subimos a los que están en la cola:
           
            self.subir_visitantes()    #la definimos de forma tal que suba automáticamente la gente de la cola
            self.reloj = self.tiempo             #reiniciamos el reloj. Si es que al subir se alcanzó el cliente 100, falla. 
                
        if not self.disponible:         #EN ESTE CASO la atracción falló y estamos esperando a que vuelva a estar disponible
            self.reparacion = self.reparacion - 1
            if self.reparacion == 0:
                self.disponible = True
                self.reparacion = 60
                self.reloj = 0          #Esto lo hacemos únicamente para que se pueda ejecutar el if que viene justo arriba 
                                        #y suban clientes
              
    def fallar(self):      
        self.disponible = False              #Se cierra la atracción. cuenta_regresiva hace que esto dure 1 hora
        
        for i in range(len(self.cola)):      #Ahora movemos a los clientes que estaban en la cola
            aux=self.cola.popleft()
            aux.elegir_atraccion()           #Los sacamos al mismo tiempo que buscan
            
        for usuario in self.usuarios:        #compensación de los que estaban jugando
            if usuario.edad >= 18:
                self.dueno.dinero = self.dueno.dinero - 10000
            elif usuario.edad < 18:
                self.dueno.dinero = self.dueno.dinero - 20000
        
        self.usuarios = []                   #los usuarios se van del parque             
        


class Visitante(Persona):                
    def __init__(self,tupla,dinero=0):      #***recibirá de input, un elemento de la lista PERSONAS. Ojo con dinero
        super().__init__(dinero)
        self.dinero= tupla[0]
        self.llegada= tupla[1]
        self.nombre= tupla[2]
        self.edad= birth_to_age(tupla[3]) 
            
            
    # def irse_dignamente(): NO ES NECESARIO DEFINIRLA, VER ÚLTIMA LÍNEA DE elegir_atraccion()        
          
    def elegir_atraccion(self):                             #buscar atracción
        opciones=[]
        print('AAA')      
        for atraccion in TheLonelyIsland.atracciones:       #***quizás esto se puede hacer con un filter. AJUSTAR NOMBRE PARQUE
            if atraccion.disponible:                    #solo buscaremos sobre las que están disponibl NO están cerradas
                opciones.append(atraccion)
        opciones.sort(key= lambda x: x.entrada)         #para ver cual es la más cara, las ordenamos de menor a mayor
        
        pagables = list(filter(lambda x: x.entrada <= self.dinero, opciones))
        
        
        if pagables:                                    #si la lista no está vacía <-> si hay elecciones pagables
            atraccion_elegida= pagables.pop()           #la de más a la derecha es la más cara
            print('{0} se sube a {1}'.format(Visitante.nombre,atraccion_elegida)  
            atraccion_elegida.aceptar_visitantes(self)  #ahora metemos al visitante a la cola de su elección     
        else:
            print('A {0} solo le quedan {1}, por lo que decide retirarse dignamente').format(self.nombre,self.dinero)
                  #***Quizás haya que hacer un Log aquí. No se hace nada más porque si no se le asigna una nueva 
                      #atracción no se almacenan en ninguna parte del parque, ergo ya no están dentro (SE RETIRARON DIGNAMENTE)



