
# coding: utf-8

# In[84]:


class pastel:
    def __init__(self, estado, ide):
        self.estado = estado
        self.vecinos = []
        self.id = ide
    def podrir(self):
        vec_sanos = [vec for vec in self.vecinos if vec.estado == 'C']
        if vec_sanos: 
            for pastel in vec_sanos:
                pastel.estado = 'P'
                podridos.append(pastel)
            #dia +=1


# In[85]:


from collections import deque
from math import sqrt

class SquareGrid:
    def __init__(self, width):
        self.width = width
        self.height = width
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1),(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = list(filter(self.in_bounds, results))
        return results


# In[86]:


g = SquareGrid(3)


# In[87]:





# In[88]:


#Asumiendo que el simpático usuario me entrega una lista de listas

#inpt = [['P','C','P'],['C','C','C'],['P','C','P']]
#Grafo = SquareGrid(len(inpt))
inppt = input('Entregue input: ')
lista = inppt.split(' ')
largo = int(sqrt(len(lista)))
fil = 0
inpt = []
while fil < len(lista):
    inpt.append(lista[fil:fil+largo])
    fil += largo
Grafo = SquareGrid(len(inpt))
pasteles = []
for i in range(len(inpt)):
    b = 0
    for k in inpt[i]:
        
        a = pastel(k,(b,i))
        pasteles.append(a)
        b+=1
def get_vecinos():
    for pastel in pasteles:
        tuplas = Grafo.neighbors(pastel.id)
        for pastel2 in pasteles:
            if pastel2.id in tuplas:
                pastel.vecinos.append(pastel2)
get_vecinos()


# In[89]:


## No es una simulacion
dia = 0
podridos = []
for i in pasteles:
    if i.estado == 'P':
        podridos.append(i)
while len(podridos) != len(pasteles):       
    podridos_a_iterar = podridos.copy()
    for pastel in podridos_a_iterar:
        pastel.podrir()
    dia +=1
print('Se demora {} días en podrir la caja'.format(dia))


# In[72]:





# In[74]:





# In[83]:




