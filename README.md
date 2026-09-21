## Estrategia

//REMPLAZAR PRIMER PARRAFO

El algoritmo utiliza una estrategia similar a **Merge Sort**

Primero, divide recursivamente el arreglo en dos mitades hasta llegar al caso base, en el que cada subarreglo contiene una sola criatura.

La estrategia principal se encuentra en la etapa de **combinación**. Una vez obtenidas las criaturas invictas de cada mitad, se comparan ambos conjuntos y se descartan 
aquellas criaturas que son dominadas por otra. De esta manera, el nuevo arreglo contiene a las criaturas invictas.

//

//REEMPLAZAR TODO LA SECCION COMBINACIÓN

## Combinación

La etapa de combinación recibe dos listas de criaturas invictas, una correspondiente a cada mitad del arreglo.

Durante el recorrido se presentan dos casos:

1. **Una criatura domina a la otra.**
   Si una de las criaturas domina a la otra, la criatura dominada se descarta y el puntero correspondiente avanza hacia la siguiente criatura. Así salta la criatura
   descartandola para que no forme parte de nuestra solución.

2. **Ninguna de las dos criaturas domina a la otra.**
   En este caso se agrega estratégicamente una de las criaturas al resultado.
   
   . Si tienen ataques diferentes, agrega la criatura con mayor ataque y avanza en su lista.
   
   . Si tienen el mismo ataque, agrega primero la de menor defensa y mantiene al frente la de mayor defensa para compararla con las criaturas siguientes.
   
   La idea es mantener en el frente una criatura que pueda ser descartada fácilmente en una comparación posterior si aparece otra que la domine, evitando conservar
   innecesariamente criaturas que no podrán ser invictas en el resultado final.


//REEMPLAZAR TODA LA SECCION


### Por qué la combinación es correcta
Funciona porque las dos listas que recibe el merge ya contienen solamente criaturas invictas de cada mitad y están ordenadas de mayor a menor ataque.

. Si las criaturas tienen ataques diferentes, se agrega la de mayor ataque. Como las criaturas que quedan tienen ataques menores o iguales, ninguna podrá dominarla posteriormente, 
porque para dominarla necesitaría tener un ataque estrictamente mayor.

. Si tienen el mismo ataque, ninguna puede dominar a la otra, aunque una tenga más defensa, porque la dominancia exige un ataque estrictamente mayor.


//QUITAR ORDENAMIENTO INICIAL Y COMBINAR CON LO YA PUESTO


### Complejidad Temporal

El algoritmo utiliza una estrategia de **divide y conquista**. El arreglo se divide en dos mitades recursivamente hasta llegar a subarreglos de un solo elemento, lo que genera una profundidad de recursión de $\log N$ niveles.

En cada nivel se realiza la etapa de **combinación**, que recorre las criaturas de las dos mitades una cantidad lineal de veces, por lo que tiene un costo de $O(N)$.

Len(array) lo tomamos como O(1).

