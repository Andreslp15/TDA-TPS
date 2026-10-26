from collections import defaultdict, deque
def agregar_arista(grafo, caudal_restante, origen, destino, capacidad):
    if destino not in caudal_restante[origen]:
        grafo[origen].append(destino)
        grafo[destino].append(origen)
        caudal_restante[origen][destino] = 0
        caudal_restante[destino][origen] = 0
    caudal_restante[origen][destino] += capacidad

def construir_red(bandas, servidores, plataformas, banda_servidor, servidor_plataforma):
    demanda = sum(capacidad for _, capacidad in bandas)
    fuente, sumidero = ("fuente",), ("sumidero",)
    grafo = defaultdict(list)
    caudal_restante = defaultdict(dict)
    capacidades_originales = defaultdict(dict)

    def conectar(origen, destino, capacidad):
        agregar_arista(grafo, caudal_restante, origen, destino, capacidad)
        capacidades_originales[origen][destino] = (
            capacidades_originales[origen].get(destino, 0) + capacidad
        )

    for banda, capacidad in bandas:
        conectar(fuente, ("banda", banda), capacidad)
    for servidor, capacidad in servidores:
        conectar(("entrada", servidor), ("salida", servidor), capacidad)
    for plataforma, capacidad in plataformas:
        conectar(("plataforma", plataforma), sumidero, capacidad)
    bandas_validas = {b for b, _ in bandas}
    servidores_validos = {s for s, _ in servidores}
    plataformas_validas = {p for p, _ in plataformas}

    for banda, servidor in banda_servidor:
        if banda not in bandas_validas or servidor not in servidores_validos:
            raise ValueError("Relacion banda-servidor desconocida")
        conectar(("banda", banda), ("entrada", servidor), demanda)

    for servidor, plataforma in servidor_plataforma:
        if servidor not in servidores_validos or plataforma not in plataformas_validas:
            raise ValueError("Relacion servidor-plataforma desconocida")
        conectar(("salida", servidor), ("plataforma", plataforma), demanda)

    return grafo, caudal_restante, capacidades_originales, fuente, sumidero, demanda


def buscar_camino(grafo, capacidad, fuente, sumidero):
    padres = {fuente: None}
    cola = deque([fuente])
    while cola and sumidero not in padres:
        actual = cola.popleft()
        for vecino in grafo[actual]:
            if vecino not in padres and capacidad[actual][vecino] > 0:
                padres[vecino] = actual
                cola.append(vecino)
                if vecino == sumidero:
                    break
    return padres if sumidero in padres else None


def aumentar_por_camino(grafo, caudal_restante, fuente, sumidero):
    padres = buscar_camino(grafo, caudal_restante, fuente, sumidero)
    if padres is None:
        return 0

    incremento = float("inf")
    actual = sumidero
    while actual != fuente:
        anterior = padres[actual]
        incremento = min(incremento, caudal_restante[anterior][actual])
        actual = anterior

    actual = sumidero
    while actual != fuente:
        anterior = padres[actual]
        caudal_restante[anterior][actual] -= incremento
        caudal_restante[actual][anterior] += incremento
        actual = anterior
    return incremento


def calcular_flujo_maximo(grafo, caudal_restante, fuente, sumidero):
    flujo_max = 0
    while True:
        incremento = aumentar_por_camino(grafo, caudal_restante, fuente, sumidero)
        if incremento == 0:
            return flujo_max
        flujo_max += incremento


def recuperar_asignacion(capacidades_originales, caudal_restante, fuente, sumidero,
                         bandas, plataformas):
    flujo_positivo = defaultdict(dict)
    for origen, vecinos in capacidades_originales.items():
        for destino, capacidad in vecinos.items():
            usado = capacidad - caudal_restante[origen][destino]
            if usado > 0:
                flujo_positivo[origen][destino] = usado

    asignacion = defaultdict(int)
    while True:
        grafo_positivo = {u: list(vecinos) for u, vecinos in flujo_positivo.items()}
        padres = buscar_camino(grafo_positivo, flujo_positivo, fuente, sumidero)
        if padres is None:
            break

        camino = []
        actual = sumidero
        cantidad = float("inf")
        while actual != fuente:
            anterior = padres[actual]
            cantidad = min(cantidad, flujo_positivo[anterior][actual])
            camino.append(actual)
            actual = anterior
        camino.append(fuente)
        camino.reverse()

        for origen, destino in zip(camino, camino[1:]):
            flujo_positivo[origen][destino] -= cantidad

        banda = next(nodo[1] for nodo in camino if nodo[0] == "banda")
        plataforma = next(nodo[1] for nodo in camino if nodo[0] == "plataforma")
        asignacion[banda, plataforma] += cantidad

    orden_bandas = {b: i for i, (b, _) in enumerate(bandas)}
    orden_plataformas = {p: i for i, (p, _) in enumerate(plataformas)}
    resultado = [(b, p, cant) for (b, p), cant in asignacion.items() if cant > 0]
    resultado.sort(key=lambda x: (orden_bandas[x[0]], orden_plataformas[x[1]]))
    return resultado


def main(bandas: list[tuple[str, int]], servidores: list[tuple[str, int]],
         plataformas: list[tuple[str, int]], banda_servidor: list[tuple[str, str]],
         servidor_plataforma: list[tuple[str, str]]) -> tuple[bool, int, list[tuple[str, str, int]]]:
    grafo, caudal_restante, originales, fuente, sumidero, demanda = construir_red(
        bandas, servidores, plataformas, banda_servidor, servidor_plataforma
    )
    flujo_max = calcular_flujo_maximo(grafo, caudal_restante, fuente, sumidero)
    asignacion = recuperar_asignacion(
        originales, caudal_restante, fuente, sumidero, bandas, plataformas
    )
    return flujo_max == demanda, flujo_max, asignacion

def actualizar_servidor(id_servidor: str, nueva_capacidad: int) -> tuple[bool, int, list[tuple[str, str, int]]]:
    raise NotImplementedError
