'''
Created on 31 oct 2024

@author: Alberto CV
'''
from Estructuras.estructuras import Lista_ordenada, Lista_ordenada_sin_repeticion, Cola, Cola_prioridad,Pila

if __name__ == '__main__':
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
    
    lista.add(3)
    print(f'Método: add(3) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    lista.add(1)
    print(f'Método: add(1) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    lista.add(3)
    print(f'Método: add(3) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    lista.add(2)
    print(f'Método: add(2) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    print("Resultado de la lista: "+ str(lista.elements())+ '\n')
    
    print(f'Método: elements() -> La lista está ordenada correctamente: ' +str(lista.elements()) + '\n')
    
    
    print("Método: remove() -> Elemento eliminado: " + str(lista.remove())+ '\n')
    
    print("Método: remove_all() -> Elementos eliminados: "+ str(lista.remove_all())+ '\n')
    
    lista.add(0)
    print(f'Método: add(0) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    lista.add(10)
    print(f'Método: add(10) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    lista.add(7)
    print(f'Método: add(7) -> Estado actual de la lista: '+ str(lista.elements())+ '\n')
    
    print(f'Método: size() -> Tamaño de la lista es el esperado: ' +str(lista.size())+ '\n')
    
    print("------------------------------------------------\n")
    
    
    
    
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
    
    lista_ordenada.add(23)
    print(f'Método: add(23) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(47)
    print(f'Método: add(47) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(47)
    print(f'Método: add(47) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(1)
    print(f'Método: add(1) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(2)
    print(f'Método: add(2) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(-3)
    print(f'Método: add(-3) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(4)
    print(f'Método: add(4) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(5)
    print(f'Método: add(5) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    print("Método: remove() -> Elemento eliminado: " + str(lista_ordenada.remove())+ '\n')
    
    print("Método: remove_all() -> Elemento eliminado: " + str(lista_ordenada.remove_all())+ '\n')
    
    lista_ordenada.add(0)
    print(f'Método: add(0) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    lista_ordenada.add(7)
    print(f'Método: add(7) -> Estado actual de la lista: '+ str(lista_ordenada.elements())+ '\n')
    
    print("------------------------------------------------\n")
    
    
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
    
    cola.add(23)
    print(f'Método: add(23) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(47)
    print(f'Método: add(47) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(1)
    print(f'Método: add(1) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(2)
    print(f'Método: add(2) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(-3)
    print(f'Método: add(-3) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(4)
    print(f'Método: add(4) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    cola.add(5)
    print(f'Método: add(5) -> Estado actual de la cola: '+ str(cola.elements())+ '\n')
    
    print("Método: remove_all() -> Elemento eliminado: " + str(cola.remove_all())+ '\n')
    
    print("------------------------------------------------\n")
    
    
    
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
    
    cola_prioridad.decrease_priority("Paciente B", 0)
    print(f'Método: decrease_priority("Paciente B", 0) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    
    # cola_prioridad.decrease_priority("Paciente B", 4)
    # print(f'Método: decrease_priority("Paciente B", 4) -> Estado actual de la cola: '+ str(cola_prioridad.elements())+ '\n')
    
    print("Método: remove() -> Paciente atendido: " + str(cola_prioridad.remove())+ '\n')
    
    print("Método: remove() -> Paciente atendido: " + str(cola_prioridad.remove())+ '\n')
    
    print("Método: remove() -> Paciente atendido: " + str(cola_prioridad.remove())+ '\n')
    
    print("------------------------------------------------\n")
    
    
    
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
    
    pila.add(1)
    print(f'Método: add(1) -> Estado actual de la cola: '+ str(pila.elements())+ '\n')
    
    pila.add(2)
    print(f'Método: add(1) -> Estado actual de la cola: '+ str(pila.elements())+ '\n')
    
    pila.add(3)
    print(f'Método: add(1) -> Estado actual de la cola: '+ str(pila.elements())+ '\n')
    
    print("Método: remove() -> Elemento eliminado: " + str(pila.remove())+ '\n')
    
    print("Método: remove_all() -> Elemento eliminado: " + str(pila.remove_all())+ '\n')
    
    print("------------------------------------------------\n")
    
    
    
    
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
