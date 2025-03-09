"""
Este ADT representa una estructura de datos lineal, específicamente un arreglo dinámico (**Arraylist**). El arreglo dinámico es una estructura de datos que permite almacenar un conjunto de elementos del mismo tipo, en la cual se puede acceder y procesar sus elementos utilizando las funciones propias de la estructura.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass, field
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic, TypeVar
from linkedlist import SingleLinked as linkedlist
# import inspect for getting the name of the current function
import inspect

T = TypeVar("T")

@dataclass
class scht(Generic[T]):
    _capacity: int = None # Tamaño inicial de la tabla
    _size: int = 0  # Número de elementos almacenados
    _buckets: List[Optional[linkedlist]] = None
    _hash_function: Callable[[T], int] = field(default_factory=lambda: hash)
    
    def __post_init__(self):
        
        if self._capacity is None:
            self._capacity = 10
            
        """Inicializa las listas enlazadas en cada bucket."""
        if self._buckets is None:
            self._buckets = [None] * self._capacity
            for i in range(self._capacity):
                self._buckets[i] = linkedlist()
            
    def _bucket_index(self, key: T) -> int:
        """Calcula el índice del bucket para una clave dada."""
        return self._hash_function(key) % self._capacity

    def insert(self, key: T, value: T) -> None:
        """Inserta un nuevo elemento en la tabla hash."""
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        bucket.add_last(value)
        self._size += 1

    def search(self, key: T) -> Optional[T]:
        """Busca un elemento en la tabla hash y devuelve su valor si se encuentra."""
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        
        #Perdon xd, ya esta tarde
        for i in range(len(bucket)):
            if bucket.get_element(i) == key:
                return bucket.get(i)
        return None
    
    
    
    def values(self) -> List[T]:
        """Devuelve una lista de todas las claves en la tabla hash."""
        values_list = linkedlist()
        for bucket in self._buckets:
            for i in range(len(bucket)):
                values_list.add_first(bucket.get_element(i))
        return values_list
    
    def __len__(self) -> int:
        """Devuelve el número de elementos en la tabla hash."""
        return self._size

    def __contains__(self, key: T) -> bool:
        """Verifica si una clave está en la tabla hash."""
        return self.search(key) is not None
    
    
