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
import linkedlist
# import inspect for getting the name of the current function
import inspect

T = TypeVar("T")

@dataclass
class scht(Generic[T]):
    _capacity: int = None # Tamaño inicial de la tabla
    _size: int = 0  # Número de elementos almacenados
    _buckets: List[Optional[linkedlist.LinkedList]] = None
    _hash_function: Callable[[T], int] = field(default_factory=lambda: hash)
    
    def __post_init__(self):
        
        if self._capacity is None:
            self._capacity = 10
            
        """Inicializa las listas enlazadas en cada bucket."""
        for i in range(self._capacity):
            
            self._buckets[i] = linkedlist.LinkedList()
        
    