from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
#from mypy.typeshed.stdlib._typeshed import SupportsAllComparisons

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R') #,SupportsAllComparisons
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: list[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        """
        Remove el primer elemento de la colección.
        :return: Elemento eliminado
        :raise IndexError: Si la colección está vacía
        """
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements



class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
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
        


class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección sin repetición.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        if e not in self._elements:
            self._elements.insert(self._index_order(e),e)
            
    def __str__(self) -> str:
        return f'ListaOrdenadaSinRepeticion({self._elements})'




class Cola(Agregado_lineal[E]):

    @classmethod

    def of(cls) -> 'Cola[E]':
        # Crea una cola vacía
        return cls()



    def add(self,e:E) -> None:
        """
        Agrega un elemento a la cola.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        
        self._elements.append(e)
        
    def __str__(self) -> str:
        return f'Cola({self._elements})'




class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        
        self._elements: list[E] = []
        
        self._priorities:list[P]= []


    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()


    def add(self, e: E, priority: P) -> None:
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        n:int=0
        
        if len(self._elements)==0:
            self._elements.append(e)
            self._priorities.append(priority)
           
        else: 
            for elemento in self._priorities:
                if priority <= elemento:
                    n+=1
                    
                else:
                    self._elements.insert(n,e)
                    self._priorities.insert(n,priority)
                    return
            self._elements.insert(n,e)
            self._priorities.insert(n,priority)
                
                
                    
        


    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        self._priorities.pop(0)
        return self._elements.pop(0)


    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad)
        """
        
        for elementos in ls:
            self.add(elementos[0], elementos[1])


    def decrease_priority(self, e: E, new_priority: P) -> None:
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        if e in self._elements:
            indice:int= self._elements.index(e)
            if new_priority<self._priorities[indice]:
                self._priorities.pop(indice)
                self._elements.pop(indice)
                self.add(e, new_priority)
                
            else:
                raise ValueError(f"La nueva prioridad con un valor de {new_priority}, no es menor que la anterior")
            
        else:
            raise ValueError(f"El elemento {e} no se encuentra en la cola de prioridad")
        
        
    def __str__(self) -> str:
        
        
        ls:list[tuple[E,P]]=[]
        for i in range(0,len(self._elements)):
            ls.append((self._elements[i],self._priorities[i]))
            
        return f'ColaPrioridad({ls})'
            




class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.

    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """
    @classmethod

    def of(cls) -> 'Pila[E]':
        # Crea una pila vacía
        return cls()
    
    def add(self,e:E) -> None:
        
        self._elements.insert(0,e)
        
    def __str__(self) -> str:
        return f'Pila ({self._elements})'
    
    


