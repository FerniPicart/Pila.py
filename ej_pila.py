from tda_dinamico_pila import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice


def cargarPila(pila):
    while(tamanio(pila) < 5):
        elemento = (input('Ingrese un elemento para añadir a la pila: '))
        apilar(pila, elemento)

lista = Pila()
cargarPila(lista)

#Ej 1
'''
buscado = int(input('Ingrese el elemento que desea buscar: '))
def ocurrencias(pila, bus):
    """
    Cuenta las veces que un objeto esta dentro de la pila.
    """
    cont = 0
    while (not pila_vacia(pila)):
        if (cima(pila) == bus):
            cont = cont + 1
        aux = desapilar(pila)
        print(aux)
    return cont
print(ocurrencias(lista, buscado))
'''

#Ej 2
'''
def eliminar_impares(pila):
    """
    Elimina elementos impares dentro de la pila.
    """
    pila_aux = Pila()
    while not pila_vacia(pila):
        e = desapilar(pila)
        apilar(pila_aux, e)
    print('pila par')
    while not pila_vacia(pila_aux):
        d = desapilar(pila_aux)
        if (d % 2 == 0):
            apilar(pila, d)
            print(d)
    return pila
print(eliminar_impares(lista))
'''

#EJ 3
'''
def reemplazar(pila, bus, otro_obj):
    """
    Reemplazar todas las ocurrencias de un determinado elemento en la pila
    """
    pila_aux = Pila()
    while not pila_vacia(pila):
        e = desapilar(pila)
        apilar(pila_aux, e)
    while not pila_vacia(pila_aux):
        d = desapilar(pila_aux)
        if (d == bus):      #si encuentra el objeto buscado, lo reemplaza por otro.
            apilar(pila, otro_obj)
        else:
            apilar(pila, d)
    return pila
print(reemplazar(lista,2,222))
'''

#Ej 4
'''
def pila_invertida(pila):
    """
    Invierte una pila.
    """
    pila_aux = Pila()
    print('Pila comun')
    while not pila_vacia(pila):
        e = desapilar(pila)
        print(e)
        apilar(pila_aux, e)
    print('pila invertida')
    while not pila_vacia(pila_aux):
        x = desapilar(pila_aux)
        print(x)
    return pila_aux
print(pila_invertida(lista))
'''

#EJ 5
'''
lista = Pila()
pila_aux = Pila()
palabra = (input('escriba una cadena de caracteres: '))
while (tamanio(lista) < len(palabra)):
    for i in range(0, len(palabra)):
        apilar(lista,palabra[i])
        apilar(pila_aux,palabra[i])
def lista_palindromo(pila,pila_aux):
    """
    Determinar si una cadena de caracteres es un palindromo
    """
    aux2 = Pila()
    print('pila invertida')
    while not pila_vacia(pila):
        e = desapilar(pila)
        apilar(aux2, e)
        print(e)
    palindromo = True
    while not (pila_vacia(pila_aux)) and not (pila_vacia(aux2)):
        a = desapilar(pila_aux)
        b = desapilar(aux2)
        if (a != b):
            palindromo = False
            print('No es palindromo')
            break
    if palindromo == True:
        print('Es un palindromo')
    return palindromo
print(lista_palindromo(lista,pila_aux))
'''

#Ej 6
'''
def palabra_inversa(palabra):
    """
    Lee la palabra dada, pero de forma invertida.
    """
    pila_aux = Pila()
    for letra in palabra:
        apilar(pila_aux, letra)
    while not pila_vacia(pila_aux):
        l = desapilar(pila_aux)
        print(l, end='')
print(palabra_inversa('hola como andas'))
'''

#ej 7
'''
eliminado = int(input('seleccione el elemento que desea eliminar: '))
def eliminar(pila, bus):
    pila_aux = Pila()
    while not pila_vacia(pila):
        e = desapilar(pila)
        if (e != bus):
            apilar(pila, e)
        if (e == bus):
            break
    while not pila_vacia(pila_aux):
        e = desapilar
        apilar(pila, e)
    return pila
#print(eliminar(lista,eliminado))
'''

#Ej 8.
'''
mazo_aux = Pila()
mazo = Pila()
espada = Pila()
basto = Pila()
copa = Pila()
oro = Pila()
palos = ['espada', 'basto', 'copa', 'oro']

while(tamanio(mazo) < 10):
    dato = ['', 0]
    dato[0] = choice(palos)
    dato[1] = randint(1, 12)
    apilar(mazo, dato)

print("Maso de cartas: ") 
while(not pila_vacia(mazo)):
    carta = desapilar(mazo)
    print(carta)
    if carta[0] == "espada":
        if(pila_vacia(espada)):
            apilar(espada, carta)
        else:
            if(cima(espada) <= carta):
                apilar(espada, carta)
            else:
                while(not pila_vacia(espada) and cima(espada) > carta):
                    daux = desapilar(espada)
                    apilar(mazo_aux, daux)
                apilar(espada, carta)
                while(not pila_vacia(mazo_aux)):
                    daux = desapilar(mazo_aux)
                    apilar(espada, daux)
    elif (carta[0] == "basto"):
        apilar(basto, carta)
    elif (carta[0] == "copa"):
        apilar(copa, carta)
    else:
        apilar(oro, carta)

print("maso espada")
while (tamanio(espada)):
    x = desapilar(espada)
    print(x)
print("maso basto")
while(tamanio(basto)):
    b = desapilar(basto)
    print(b)
print("maso copa")
while(tamanio(copa)):  
    c = desapilar(copa)
    print(c)
print("maso oro")
while(tamanio(oro)):
    o = desapilar(oro)
    print(o)
'''

#Ej 9
'''
numero = int(input('ingrese el numero a aplicar el Factorial: '))
def factorial(numero):
    """
    Resuelve factorial de un numero dado.
    """
    i = 0
    fac = 1
    pila = Pila()
    for i in range(numero):
        apilar(pila, i+1)
    while not pila_vacia(pila):
        x = desapilar(pila)
        fac = x * fac
    return fac
print(factorial(numero))
'''

#Ej 10. 
'''
def dioses(pila):
    piladioses = Pila()
    while (tamanio(pila) < 5):
        nom = input('ingrese el nombre del Dios a guardar: ')
        apilar(pila, nom)
#####
piladioses = Pila()
dioses(piladioses)
nombre = 'Atenea'
puesto = int(input('ingrese puesto donde se guardara: '+ nombre))
#####
def insertar(pila,personaje,puesto):
    """
    Inserta en una pila el nombre dado y en la posicion requerida
    """
    pila_aux = Pila()
    for i in range(puesto):
        x = desapilar(pila)
        apilar(pila_aux, x)
    apilar(pila, personaje)
    while not pila_vacia(pila_aux):
        p = desapilar(pila_aux)
        apilar(pila, p)
    return pila
#print(insertar(piladioses,nombre,puesto))
'''

#Ej 11.
'''
letras = Pila()
def pila_letras(letras):
    n = int(input('presione 1 para agregar letra, 2 para salir: '))
    if (n == 1):
        letras = str(input('ingrese una letra: '))
    return letras
def contar_vocales(pila):
    """
    Cuenta las vocales que hay dentro de una pila de letras.
    """
    vocales = ('a','e','i','o','u','A','E','I','O','U')
    cont = 0
    while not pila_vacia(pila):
        letra = desapilar(pila)
        if letra in vocales:
            cont += 1
    return cont
print(contar_vocales(letras))
'''

#Ej 12.
'''
# Dada una pila con nombres de los personajes de la saga de Star Wars, 
# implemente una función que permita determinar si Leia Organa 
# o Boba Fett están en dicha pila sin perder los datos.
def personajes(pila):
    """
    determinar si Leia Organa o Boba Fett están en dicha pila
    """
    pila_aux = Pila()
    cond1 = False
    cond2 = False
    while not pila_vacia(pila):
        nom = desapilar(pila)
        if (nom == 'Leia Organa'):
            cond1 = True
        elif (nom == 'Boba Fett'):
            cond2 = True
        apilar(pila_aux, nom)
    while not pila_vacia(pila_aux):
        n = desapilar(pila_aux)
        apilar(pila, n)
    print('1- Leia Organa. 2- Bobba Fett')
    
    return cond1, cond2
'''

#Ej 13.
'''
def ordenar_creciente(pila):
    """
    Ordena de forma creciente, los datos de una pila.
    """
    if not pila_vacia(pila):
        condicion = True

        while condicion:
            pila_aux = Pila()
            condicion = False
            aux = desapilar(pila)
            while not pila_vacia(pila):
                elem = desapilar(pila)
                if elem > aux:
                    apilar(pila_aux, elem)
                    condicion = True
                else:
                    apilar(pila_aux, aux)
                    aux = elem

            while not pila_vacia(pila_aux):
                elem = desapilar(pila_aux)
                if elem < aux:
                    apilar(pila, elem)
                    condicion = True
                else:
                    apilar(pila, aux)
                    aux = elem
            apilar(pila, aux)
    return pila
print(ordenar_creciente(lista))
'''

#Ej 14. Hecho en pila comun
'''
def quicksort(pila,pri,ult):
    """
    Metodo de ordenamiento.
    """
    pila_aux = Pila()
    apilar(pila_aux, [pri,ult])
    datos = []
    while not pila_vacia(pila_aux):
        datos = desapilar(pila_aux)
        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]
        while (i < j):
            while (pila[i] <= pila[pivot]) and (i < j):
                i += 1
            while (pila[j] > pila[pivot]) and (i < j):
                j -= 1
            if i <= j:
                pila[i], pila[j] = pila[j], pila[i]
        if pila[pivot] < pila[i]:
            pila[pivot], pila[i] = pila[i], pila[pivot]
        if datos[0] < j:
            apilar(pila_aux, [datos[0], j])
        if datos[1] > i:
            apilar(pila_aux, [i+1, datos[1]])
'''

#Ej 15
'''
#Llamar funcion cargarPila
cap5 = Pila()
cargarPila(cap5)
cap7 = Pila()
cargarPila(cap7)
def StarWars(Cap5,Cap7):
    """
    Guarda objetos de 2 pilas en 1. En este caso personajes de Star Wars.
    """
    p_ambas = Pila()
    while not pila_vacia(Cap5):
        pj = desapilar(Cap5)
        apilar(p_ambas, pj)
    while not pila_vacia(cap7):
        x = desapilar(Cap7)
        apilar(p_ambas, x)
    print('ambas pilas en una')
    while not pila_vacia(p_ambas):
        print(desapilar(p_ambas))
    return p_ambas
print(StarWars(cap5,cap7))
'''

#Ej 16.
'''
#Variables
parrafo = (input('escriba un texto: '))
numeros = '0123456789'
vocales = 'AaEeIiOoUu'
consonantes = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
pila = Pila()
voc = Pila()
cons = Pila()
otros = Pila()
caract = 0
cont_num = 0
cont_vocal = 0
cont_consonantes = 0
cont_otros = 0
zeta = False
espacios = 0

#Cuerpo
while (tamanio(pila) < len(parrafo)):
    for i in range(0, len(parrafo)):
        apilar(pila,parrafo[i])
while not pila_vacia(pila):
    char = desapilar(pila)
    caract += 1
    if (char in vocales):
        apilar(voc,char)
        cont_vocal += 1
    elif (char in consonantes):
        apilar(cons,char)
        if (char == 'z') or (char == 'Z'):
            zeta = True
        cont_consonantes += 1
    else:
        apilar(otros,char)
        if (char in numeros):
            cont_num += 1
        else:
            cont_otros += 1
            if (char == ' '):
                espacios += 1
#impresiones
porcentaje = (((cont_vocal / cont_consonantes) *100) /2)
if (cont_vocal == cont_consonantes):
    print ('cantidad de vocales es igual a cantidad de consonantes')
if (cont_vocal == caract):
    print('cantidad de vocales igual a la de caracteres')
if (zeta == True):
    print('Hay almenos una "Z" en el parrafo')
else:
    print('No hay "Z" en el parrafo')
print('Cantidad de Vocales: ' ,cont_vocal)
print('Cantidad Consonantes: ' , cont_consonantes)
print('Cantidad Numeros: ',cont_num)
print('Cantidad Otros caracteres: ' ,cont_otros)
print('Cantidad de espacios:' ,espacios)
print('Porcentaje de vocales sobre consonantes: ' ,porcentaje)
'''

#Ej 17. 
'''
#Carga los datos
oficina = ['mause', 'monitor', 'silla', 'teclado', 'cpu', 'camara Web']
pila = Pila()
while (tamanio(pila) < 10):
    dato = ['',0]
    dato[0] = choice(oficina)
    dato[1] = randint(1,100)
    apilar(pila,dato)
"""
Ordena elementos por su 2da caracteristica, en este caso el peso de los objetos de una oficina.
"""
pila_aux = Pila()
pila_ordenada = Pila()

while (not pila_vacia(pila)):
    aux = desapilar(pila)
    while not pila_vacia(pila_ordenada) and (aux[1] < cima(pila_ordenada)[1]):
        obj = desapilar(pila_ordenada)
        apilar(pila_aux,obj)
    apilar(pila_ordenada,aux)

    while not pila_vacia(pila_aux):
        obj = desapilar(pila_aux)
        apilar(pila_ordenada, obj)

print ('..pila ordenada..')
while not pila_vacia(pila_ordenada):
    print(desapilar(pila_ordenada))
'''

#Ej 18
'''
pila_peliculas = Pila()
pila_marvel = Pila()
pila_2014 = Pila()
cont_2018 = 0

titulo = input('titulo: ')
while titulo != '':
    estreno = int(input('año: '))
    estudio = input('estudio cinematografico: ')
    apilar(pila_peliculas,[titulo, estreno, estudio])
    titulo = input('titulo: ')

while not pila_vacia(pila_peliculas):
    dato = desapilar(pila_peliculas)
    if str(dato[1]) == '2014':
        apilar(pila_2014,dato)
    elif str(dato[1]) == '2018':
        cont_2018 += 1
    elif str(dato[1]) == '2016' and dato[2] == 'Marvel Studios':
        apilar(pila_marvel,dato)
    
print('cantidad de peliculas estrenadas en 2018: ', cont_2018)
print('peliculas estrenadas en 2014: ')
while not pila_vacia(pila_2014):
    x = desapilar(pila_2014)
    print(x[0])

print('peliculas estrenadas en 2016 por Marvel Studios: ')
while not pila_vacia(pila_marvel):
    x = desapilar(pila_marvel) 
    print(x[0])
'''

#Ej 19 
'''
cond = 'y'
cont_pasos = 0
movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'noroeste', 'sureste', 'suroeste']

while (cond == 'y'):
    apilar(pila, choice(movimientos))
    cont_pasos += 1 
    cond = input('presione "y" para continuar cargando: ')

print('pasos realizados: ')
while not pila_vacia(pila):
    x = desapilar(pila)
    apilar(pila_aux,x)
    print(x)

while not pila_vacia(pila_aux):
    apilar(pila,desapilar(pila_aux))
while not pila_vacia(pila):
    x = desapilar(pila)
    if x == 'norte':
        apilar(pila_aux, 'sur')
    elif x == 'sur':
        apilar(pila_aux, 'norte')
    elif x == 'este':
        apilar(pila_aux, 'oeste')
    elif x == 'oeste':
        apilar(pila_aux, 'este')
    elif x == 'norte':
        apilar(pila_aux, 'sur')
    elif x == 'noreste':
        apilar(pila_aux, 'suroeste')
    elif x == 'noroeste':
        apilar(pila_aux, 'sureste')
    elif x == 'sureste':
        apilar(pila_aux, 'noroeste')
    elif x == 'suroeste':
        apilar(pila_aux, 'noreste')

while not pila_vacia(pila_aux):
    apilar(pila,desapilar(pila_aux))

print('pasos realizados para volver al punto de partida:')
while not pila_vacia(pila):
    print(desapilar(pila))

print('el robot realiza una cantidad de ', cont_pasos,' pasos de ida')
print('el robot realiza en total ', cont_pasos*2,' de pasos en ida y vuelta')
'''


#Ej 20.
'''
def fibonacci(numero, pila):
    if numero == 1: 
        return 0
    elif numero == 2: 
        return 1
    else:
        numero -= 2
        apilar(pila, 0)
        apilar(pila, 1)
        while numero > 0:
            #sacamos el ultimo
            cim = desapilar(pila)
            #tambien sacamos el anteultimo
            cim_2 = desapilar(pila)
            #calculamos el actual
            n_actual = cim + cim_2 
            
            #metemos los 3
            apilar(pila, cim_2) 
            apilar(pila, cim)
            apilar(pila, n_actual)
            
            numero -= 1
        return cima(pila)

print(fibonacci(8, pila))
'''

#Ej 21. 
'''
abril = Pila()
cant = 0
while (tamanio(abril) < 6):
    cant += 1
    dato = randint(0,30)
    apilar(abril,dato)

pila_aux = Pila()
prom = 0
max = 0
min = 40
while not pila_vacia(abril):
    x = desapilar(abril)
    apilar (pila_aux, x)
    if (max < x):
        max = x
    if (min > x):
        min = x
    prom += x
prom = prom / cant
encima = 0
debajo = 0
while not pila_vacia(pila_aux):
    y = desapilar(pila_aux)
    apilar(abril, y)
    if (prom < y):
        encima += 1
    else:
        debajo += 1
print ('Minima: ' ,min)
print ('Maxima: ' ,max)
print ('Promedio temperatura: ' ,prom)
print ('Dias por debajo de la media: ' ,debajo)
print ('Dias por Encima: ' ,encima)
print ('Pila real')
while not pila_vacia(abril):
    print(desapilar(abril))
'''

#Ej 22
'''
personajes = Pila()
personajes = ['Groot' , 'Magneto' , 'Iron Man' , 'Rocket Raccoon' , 'Sam' ,'Black Widow' , 'Bruce Banner']
lista = Pila()
while (tamanio(lista)) < 7:
    dato = ['',0]
    dato[0] = choice(personajes)
    dato[1] = randint(1,10)
    apilar(lista,dato)

def personajes_marvel(pila_personajes):
    i = 1
    while (not (pila_vacia(pila_personajes))):
        personaje = desapilar(pila_personajes)
        if (personaje[0] == 'Rocket Raccoon' or personaje[0] == 'Groot'):
            print(personaje[0], 'esta en la posición', i+1)
        if (personaje[1] > 5):
            print(personaje[0], 'participo en mas de 5 peliculas')
        if (personaje[0] == 'Black Widow'):
            print(personaje[0], 'participo en', personaje[1], 'peliculas')
        if (personaje[0][0] in ['C','D','G']):
            print ('comienza con C, D o G: ',personaje[0])
        i += 1
    return
print(personajes_marvel(lista))
'''