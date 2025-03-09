from dataclasses import dataclass, field
from typing import List, Optional, Callable, Generic, TypeVar
from linkedlist import SingleLinked as linkedlist

T = TypeVar("T")

@dataclass
class scht(Generic[T]):
    _capacity: int = None # Tamaño inicial de la tabla
    _size: int = 0  # Número de elementos almacenados
    _buckets: List[Optional[linkedlist]] = None
    
    #Función hash por defecto, cambiarla por la del curso.
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

    def put(self, key: T, value: T) -> None:
        """Inserta un par clave-valor en la tabla hash."""
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        
        for i in range(len(bucket)):
            if bucket.get_element(i)[0] == key:
                bucket.get_element(i)[1] = value
                return
        
        bucket.add_first((key, value))
        self._size += 1

    def get(self, key: T) -> Optional[T]:
        """Devuelve el valor asociado con una clave en la tabla hash."""
        index = self._bucket_index(key)
        bucket = self._buckets[index]
        
        for i in range(len(bucket)):
            if bucket.get_element(i)[0] == key:
                return bucket.get_element(i)[1]
        
        return None
    
    def keys(self) -> List[T]:
        """Devuelve una lista de todas las claves en la tabla hash."""
        keys_list = linkedlist()
        for bucket in self._buckets:
            for i in range(len(bucket)):
                keys_list.add_first(bucket.get_element(i)[0])
        return keys_list
    
    
    
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
    
    

if __name__ == "__main__":
    # Crear una tabla hash con capacidad inicial de 5
    hash_table = scht[int](_capacity=5)

        # Insertar elementos en la tabla hash
    hash_table.put(1, "uno")
    hash_table.put(2, "dos")
    hash_table.put(3, "tres")
    hash_table.put(4, "Colombia")

    print(hash_table.keys())
    # Buscar elementos en la tabla hash
    print("Buscando elementos en la tabla hash:")
    print(hash_table.get(1))  # Salida: "uno"
    print(hash_table.get(4))  # Salida: Colombia
    print(hash_table.get(5))  # Salida: None

    #print(hash_table.values()) #Otra lista similar a keys pero con las llaves.
        # Verificar el tamaño de la tabla hash
    print(len(hash_table))  # Salida: 4