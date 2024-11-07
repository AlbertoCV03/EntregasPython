'''
Created on 31 oct 2024

@author: Alberto CV
'''
from Estructuras.estructuras import Lista_ordenada, Lista_ordenada_sin_repeticion, Cola, Cola_prioridad,Pila

def test_lista_ordenada():
        print("------------------------------------------------")
        print()
        print("TEST DE LISTA ORDENADA")
        print()
        print("------------------------------------------------")
        print()
        print("Objetivo: La Lista Ordenada mantiene los elementos en un orden específico, definido por un criterio. En este caso, se ordena de menor a mayor.")
        print()
        print("------------------------------------------------")
        print("Elementos a agregar: [3, 1, 3, 2] \n")
        
        lista:Lista_ordenada = Lista_ordenada(lambda x: x)
        
        a = 3
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        a = 1
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        a = 3
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        a = 2
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        
        print(f'Resultado de la lista: {lista.elements()} \n')
        
        print(f'Método: elements() -> La lista está ordenada correctamente: {lista.elements()} \n')
        
        
        print(f'Representación como cadena: {lista}\n')
        
        
        print(f'Método: remove() -> Elemento eliminado: {lista.remove()} \n')
        
        print(f'Método: remove_all() -> Elementos eliminados: {lista.remove_all()} \n')
        
        a = 0
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        a = 10
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        a = 7
        lista.add(a)
        print(f'Método: add({a}) -> Estado actual de la lista: {lista.elements()}\n')
    
        print(f'Método: size() -> Tamaño de la lista es el esperado: {lista.size()}\n')
    
        print("------------------------------------------------\n")
        
def test_lista_ordenada_sin_repeticion():
    
    print("------------------------------------------------")
    print()
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN")
    print()
    print("------------------------------------------------")
    print()
    print(f"Objetivo: La Lista Ordenada Sin Repetición mantiene los elementos en orden sin permitir duplicados.\
    \nEn este caso, se ordena de mayor a menor.")
    print()
    print("------------------------------------------------")
    print("Elementos a agregar: [23, 47, 47, 1, 2, -3, 4, 5] \n")
    
    
    lista_ordenada:Lista_ordenada_sin_repeticion = Lista_ordenada_sin_repeticion(lambda x: -x)
    
    a = 23
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 47
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 47
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 1
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 2
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = -3
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 4
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')

    a = 5
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')
    
    print(f'Representación como cadena: {lista_ordenada}\n')
    
    print(f'Método: remove() -> Elemento eliminado: {lista_ordenada.remove()} \n')
    
    print(f'Método: remove_all() -> Elementos eliminados: {lista_ordenada.remove_all()}\n')
    
    a = 0
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')
    
    a = 7
    lista_ordenada.add(a)
    print(f'Método: add({a}) -> Estado actual de la lista: {lista_ordenada.elements()}\n')
    
    print("------------------------------------------------\n")
    
    
def test_cola():
    
    print("------------------------------------------------")
    print()
    print("TEST DE COLA")
    print()
    print("------------------------------------------------")
    print()
    print(f"Objetivo: La Cola funciona bajo el principio de primero en entrar, primero en salir (FIFO).")
    print()
    print("------------------------------------------------")
    print("Elementos a agregar: [23, 47, 1, 2, -3, 4, 5] \n")
    
    cola:Cola = Cola.of()
    
    a = 23
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = 47
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = 1
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = 2
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = -3
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = 4
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')

    a = 5
    cola.add(a)
    print(f'Método: add({a}) -> Estado actual de la cola: {cola.elements()}\n')
    
    print(f'Representación como cadena: {cola}\n')
    
    print(f'"Método: remove_all() -> Elemento eliminado: {cola.remove_all()}\n')
    
    print("------------------------------------------------\n")
    
def test_cola_prioridad():
    
    print("------------------------------------------------")
    print()
    print("TEST DE COLA DE PRIORIDAD")
    print()
    print("------------------------------------------------")
    print()
    print(f"Objetivo: La Cola de Prioridad permite atender elementos con mayor prioridad antes que otros.")
    print()
    print("------------------------------------------------")
    print("Pacientes a agregar: [('Paciente A', 3), ('Paciente C', 1), ('Paciente B', 2)] \n")
    
    cola_prioridad:Cola_prioridad = Cola_prioridad()
    
    cola_prioridad.add("Paciente A", 3)
    print(f'Método: add("Paciente A", 3) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    cola_prioridad.add("Paciente C", 1)
    print(f'Método: add("Paciente C", 1) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    cola_prioridad.add("Paciente B", 2)
    print(f'Método: add("Paciente B", 2) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    print(f'Representación como cadena: {cola_prioridad}\n')
    
    cola_prioridad.decrease_priority("Paciente B", 0)
    print(f'Método: decrease_priority("Paciente B", 0) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n') 
    
    try:
        cola_prioridad.decrease_priority("Paciente B", 4)
    except Exception as e:
        print(f'Error: {e}\n')
        
        
    print(f'Método: decrease_priority("Paciente B", 4) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    print(f'Método: remove() -> Paciente atendido: {cola_prioridad.remove()}\n')
    
    print(f'Método: remove() -> Paciente atendido: {cola_prioridad.remove()}\n')
    
    print(f'Método: remove() -> Paciente atendido: {cola_prioridad.remove()}\n')
    
    print("------------------------------------------------\n")
    
    
def test_pila():
    
    print("------------------------------------------------")
    print()
    print("TEST DE PILA")
    print()
    print("------------------------------------------------")
    print()
    print(f"Objetivo: La Pila sigue el principio de último en entrar, primero en salir (LIFO).")
    print()
    print("------------------------------------------------")
    print("Elementos a agregar: [1, 2, 3] \n")
    
    
    pila:Pila = Pila()
    
    a = 1
    pila.add(a)
    print(f'Método: add({a}) -> Estado actual de la pila: {pila.elements()}\n')

    a = 2
    pila.add(a)
    print(f'Método: add({a}) -> Estado actual de la pila: {pila.elements()}\n')

    a = 3
    pila.add(a)
    print(f'Método: add({a}) -> Estado actual de la pila: {pila.elements()}\n')
    
    print(f'Representación como cadena: {pila}\n')
    
    print(f'Método: remove() -> Elemento eliminado: {pila.remove()}\n')
    
    print(f'Método: remove_all() -> Elementos eliminados: {pila.remove_all()}\n')
    
    print("------------------------------------------------\n")
    


    
    
    

if __name__ == '__main__':
    
    test_lista_ordenada()
    test_lista_ordenada_sin_repeticion()
    test_cola()
    test_cola_prioridad()
    test_pila()
    
    
    
    
    
    
    
    
    
   
    
   
    
    
    # lista:Lista_ordenada = Lista_ordenada(lambda x: x)
    # lista.add(5)
    # lista.add(2)
    # lista.add(8)
    # print(lista.elements())  # Salida: [2, 5, 8]
    #
    # print('___________________________________________________________')
    #
    # lista = Lista_ordenada_sin_repeticion(lambda x: -x)
    # lista.add(5)
    # lista.add(2)
    # lista.add(5)  # Este 5 no se añadirá porque ya existe
    # print(lista.elements())  # Salida: [5, 2]
    #
    # print('___________________________________________________________')
    #
    # cola:Cola = Cola.of()
    # cola.add("Juan")    # Juan llega primero
    # cola.add("María")   # María llega segunda
    # cola.add("Pedro")   # Pedro llega tercero
    # print(cola.elements())
    # print(cola.remove())  # Sale "Juan" porque llegó primero
    # print(cola.remove())  # Sale "María" porque era la siguiente
    # print(cola.elements())
    #
    # print('___________________________________________________________')
    #
    # cola_prioridad:Cola_prioridad = Cola_prioridad()
    # cola_prioridad.add("Tarea normal", 1)
    # cola_prioridad.add("Emergencia", 10)
    # cola_prioridad.add("Puede esperar", 0)
    # print(cola_prioridad.elements())
    #
    # print(cola_prioridad.remove())
    #
    # print(cola_prioridad.elements())
    # print(cola_prioridad._priorities)
    # cola_prioridad.add("Emergencia", 9)
    # print(cola_prioridad.elements())
    #
    # ls:list[tuple[str,int]]=[("Tarea especial",7),("Tarea crítica",8),("Nivel 0",0)]
    # cola_prioridad.add_all(ls)
    # print(cola_prioridad.elements())
    # print(cola_prioridad._priorities)
    #
    # cola_prioridad.decrease_priority("Tarea crítica", 6)
    # print(cola_prioridad.elements())
    # print(cola_prioridad._priorities)
    #
    # print('___________________________________________________________')
    #
    # pila:Pila = Pila()
    # pila.add("Plato 1")
    # pila.add("Plato 2")
    # pila.add("Plato 3")
    # print(pila.remove())  # Sale "Plato 3" porque fue el último en entrar
    # print(pila.remove())  # Sale "Plato 2"
    #
    #
