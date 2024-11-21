'''
Created on 21 nov 2024

@author: Alberto CV
'''

from __future__ import annotations
from Estructuras.estructuras import Lista_ordenada, Lista_ordenada_sin_repeticion, Cola, Cola_prioridad,Pila,\
    Agregado_lineal
    
from typing import List, TypeVar, Generic, Callable, Tuple, Optional
from abc import ABC, abstractmethod

E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')


class ColaConLimite(Agregado_lineal):
    
    def __init__(self,capacidad:int)->ColaConLimite:
        super().__init__()
        self.capacidad = capacidad
        
    def add(self,e:E):
        if self.size()<self.capacidad:
            
            self._elements.append(e)
        else:
            raise OverflowError('La cola ya esta llena, no puedes agregar nuevos elementos \n')
        
    @classmethod
    def of(cls,capacidad:int) -> ColaConLimite:
        
        if capacidad>0:
            return cls(capacidad)
        
        else:
            raise Exception('No puedes crear una cola sin elementos \n')
    
    def is_full(self)->bool:
        if self.size()==self.capacidad:
            return True
        
        else:
            return False
        
def test_ColaConLimite():
    try: 
        ColaConLimite.of(-3)
        
    except Exception as e: 
        print(e)
        
    cola = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    
    print(f'Estado actual de la cola {cola.elements()} \n')
    
    print(f'¿La cola esta llena? {cola.is_full()}\n')
    
    try: 
        cola.add("Tarea 4")
        
    except OverflowError as e: 
        print(e)
        
    print(f'Eliminamos el primer elemento introducido {cola.remove()} \n')
    
    print(f'¿La cola esta llena? {cola.is_full()}\n')
    
    print('Fin del testeo de ColaConLimite')
    print('___________________________________________________________________________________')
    
class Agregado_lineal2(ABC, Generic[E]):

    def __init__(self):
        self._elements: list[E] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements
    
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        
        for element in self._elements:
            if func(element):
                return element
        return None
    
    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]
    
    
def test_agregado_lineal2():
    
    class Lista_ordenada(Agregado_lineal2[E], Generic[E, R]):
        def __init__(self, order: Callable[[E], R]):
            # Inicializa la colección con una función de ordenación
            super().__init__()
            self._order = order
    
        @classmethod
        def of(cls,order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
            """
            Crea una instancia de la clase lista ordenada.
            :param order: Función de ordenación
            :return: Instancia de Lista_ordenada
            """
            
            return cls(order)
    
        def _index_order(self, e: E) -> int:
            """
            Busca el índice correspondiente a un elemento en la colección.
            :param e: Elemento a buscar
            :return: int
            """
            n:int=0
            
            for elemento in self._elements:
                if self._order(e)<= self._order(elemento):
                    return n
                n+=1
            # for i, elemento in enumerate(self._elements):
            #     if self._order(e) <= self._order(elemento):
            #         return i
            return len(self._elements)
    
        def add(self, e: E) -> None:
            """
            Inserta un elemento en el lugar correspondiente
            :param e: Elemento a agregar
            """
            
            self._elements.insert(self._index_order(e),e)
            
        def __str__(self) -> str:
            return f'ListaOrdenada({self._elements})'
            

    
    
    lista:Lista_ordenada = Lista_ordenada(lambda x: x)
    a = 3
    lista.add(a)
    a = 1
    lista.add(a)
    
    a = 2
    lista.add(a)
    a = 4
    lista.add(a)
    print(f'Estado actual de la lista: {lista.elements()}\n')
    
    a=2
    print(f'¿Contiene la lista el elemento {a}? {lista.contains(a)} \n')
    a=4
    print(f'¿Contiene la lista el elemento {a}? {lista.contains(a)} \n')
    
    print(f'Encuentra el primer elemento par: {lista.find(lambda x:x%2==0)} \n')
    
    print(f'Encuentra el primer elemento divisible por 7: {lista.find(lambda x:x%7==0)} \n')
    
    print(f'Devuelve una lista con solo los elementos pares: {lista.filter(lambda x:x%2==0)} \n')
    
    print(f'Devuelve una lista con solo los elementos divisibles por 7: {lista.filter(lambda x:x%7==0)} \n')
    
    
    

if __name__ == '__main__':
    test_ColaConLimite()
    test_agregado_lineal2()