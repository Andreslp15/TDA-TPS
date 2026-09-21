def es_compatible(prenda, lavarropas, incompatibilidades):
    for otra_prenda in lavarropas:
        if otra_prenda in incompatibilidades[prenda]:
            return False
    return True

def buscar_prendas_forzadas(pos, pendientes_por_grado, lavarropas, incompatibilidades):
    forzadas = []

    # Buscar prendas que no pueden entrar en ningun lavarropas ya usado
    for i in range(pos, len(pendientes_por_grado)):
        prenda = pendientes_por_grado[i]
        puede_entrar = False

        for lavarropas_actual in lavarropas:
            if es_compatible(prenda, lavarropas_actual, incompatibilidades):
                puede_entrar = True
                break

        if not puede_entrar:
            forzadas.append(prenda)

    return forzadas

def seleccionar_incompatibles_entre_si(prendas, incompatibilidades):
    # Armar un subconjunto de prendas forzadas mutuamente incompatibles
    incompatibles_entre_si = []

    for prenda in prendas:
        incompatible_con_todas = True

        for otra in incompatibles_entre_si:
            if otra not in incompatibilidades[prenda]:
                incompatible_con_todas = False
                break

        if incompatible_con_todas:
            incompatibles_entre_si.append(prenda)

    return incompatibles_entre_si

def calcular_bound(pos, pendientes_por_grado, lavarropas, incompatibilidades):
    forzadas = buscar_prendas_forzadas(
        pos, pendientes_por_grado, lavarropas, incompatibilidades
    )
    incompatibles_entre_si = seleccionar_incompatibles_entre_si(
        forzadas, incompatibilidades
    )
    return len(lavarropas) + len(incompatibles_entre_si)

def asignar_por_bloques(
    pos,
    pendientes_por_grado,
    lavarropas,
    asignacion_actual,
    mejor_estado,
    incompatibilidades
):
    n = len(pendientes_por_grado)

    if pos == n:
        if len(lavarropas) < mejor_estado["cantidad"]:
            mejor_estado["cantidad"] = len(lavarropas)
            mejor_estado["asignacion"] = asignacion_actual.copy()
        return

    cota = calcular_bound(
        pos,
        pendientes_por_grado,
        lavarropas,
        incompatibilidades
    )

    if cota >= mejor_estado["cantidad"]:
        return

    prenda = pendientes_por_grado[pos]

    probar_lavarropas_existentes(
        prenda,
        pos,
        pendientes_por_grado,
        lavarropas,
        asignacion_actual,
        mejor_estado,
        incompatibilidades
    )
    probar_lavarropas_nuevo(
        prenda,
        pos,
        pendientes_por_grado,
        lavarropas,
        asignacion_actual,
        mejor_estado,
        incompatibilidades
    )

def probar_lavarropas_existentes(
    prenda,
    pos,
    pendientes_por_grado,
    lavarropas,
    asignacion_actual,
    mejor_estado,
    incompatibilidades
):
    for i in range(len(lavarropas)):
        if es_compatible(prenda, lavarropas[i], incompatibilidades):
            lavarropas[i].append(prenda)
            asignacion_actual[prenda] = i

            asignar_por_bloques(
                pos + 1,
                pendientes_por_grado,
                lavarropas,
                asignacion_actual,
                mejor_estado,
                incompatibilidades
            )

            # Sacar prenda de lavarropas[i]
            lavarropas[i].pop()
            del asignacion_actual[prenda]

def probar_lavarropas_nuevo(
    prenda,
    pos,
    pendientes_por_grado,
    lavarropas,
    asignacion_actual,
    mejor_estado,
    incompatibilidades
):
    if len(lavarropas) + 1 < mejor_estado["cantidad"]:
        nuevo_lavarropas = [prenda]
        indice_nuevo = len(lavarropas)

        lavarropas.append(nuevo_lavarropas)
        asignacion_actual[prenda] = indice_nuevo

        asignar_por_bloques(
            pos + 1,
            pendientes_por_grado,
            lavarropas,
            asignacion_actual,
            mejor_estado,
            incompatibilidades
        )

        del asignacion_actual[prenda]
        lavarropas.pop()

def ordenar_prendas_por_grado(cant_prendas, incompatibilidades):
    pendientes_por_grado = []
    grados = {}
    for prenda in range(1, cant_prendas + 1):
        pendientes_por_grado.append(prenda)
        grados[prenda] = len(incompatibilidades[prenda])

    # Primero se procesan las prendas con mas incompatibilidades
    pendientes_por_grado.sort(
        key=grados.get,
        reverse=True
    )

    return pendientes_por_grado

def generar_etiqueta(indice):
    etiqueta = ""
    numero = indice + 1

    while numero > 0:
        numero, resto = divmod(numero - 1, 26)
        etiqueta = chr(ord("A") + resto) + etiqueta

    return etiqueta

def construir_resultado(asignacion):
    resultado = []
    for prenda in sorted(asignacion.keys()):
        idx_lav = asignacion[prenda]
        resultado.append((prenda, generar_etiqueta(idx_lav)))

    return resultado

def resolver_lavanderia(cant_prendas: int, incompatibilidades: dict) -> list[tuple[int, int]]:
    pendientes_por_grado = ordenar_prendas_por_grado(cant_prendas, incompatibilidades)
    lavarropas = []
    asignacion_actual = {}

    mejor_estado = {
        "cantidad": cant_prendas + 1,
        "asignacion": {}
    }

    asignar_por_bloques(
        0,
        pendientes_por_grado,
        lavarropas,
        asignacion_actual,
        mejor_estado,
        incompatibilidades
    )

    return construir_resultado(mejor_estado["asignacion"])

def main(filepath: str) -> list[tuple[int, int]]:
    cant_prendas = 0
    incompatibilidades = {}

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if parts[0] == 'p':
                cant_prendas = int(parts[1])
                for i in range(1, cant_prendas + 1):
                    incompatibilidades[i] = set()
            elif parts[0] == 'e':
                u, v = int(parts[1]), int(parts[2])
                incompatibilidades[u].add(v)
                incompatibilidades[v].add(u)

    return resolver_lavanderia(cant_prendas, incompatibilidades)
