DEFENSA_MINIMA_POSIBLE = -1
POSICION_INICIAL = 0

def combinar_frentes(frente_izq: list[tuple[int, int]], frente_der: list[tuple[int, int]]) -> list[tuple[int, int]]:
    frente_activo = []

    frente_activo.extend(frente_izq)

    maxima_defensa_enemigos_mas_fuertes = DEFENSA_MINIMA_POSIBLE
    posicion_izq = POSICION_INICIAL
    total_criaturas_izq = len(frente_izq)

    for criatura_der in frente_der:
        ataque_der, defensa_der = criatura_der

        while posicion_izq < total_criaturas_izq and frente_izq[posicion_izq][0] > ataque_der:
            defensa_izq = frente_izq[posicion_izq][1]
            maxima_defensa_enemigos_mas_fuertes = max(maxima_defensa_enemigos_mas_fuertes, defensa_izq)
            posicion_izq += 1

        if maxima_defensa_enemigos_mas_fuertes < defensa_der:
            frente_activo.append(criatura_der)

    return frente_activo

def _obtener_invictas_recursivo(criaturas: list[tuple[int, int]], inicio: int = 0, fin: int = None) -> list[
    tuple[int, int]]:
    if fin is None:
        fin = len(criaturas)

    # Caso base
    if fin - inicio <= 1:
        return criaturas[inicio:fin]

    # Division
    mitad = (inicio + fin) // 2

    # Conquista
    frente_izq = _obtener_invictas_recursivo(criaturas, inicio, mitad)
    frente_der = _obtener_invictas_recursivo(criaturas, mitad, fin)

    # Combinacion
    return combinar_frentes(frente_izq, frente_der)


def main(criaturas: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], int]:
    if not criaturas:
        return [], 0

    criaturas_ordenadas = sorted(criaturas, key=lambda c: (-c[0], -c[1]))

    invictas = _obtener_invictas_recursivo(criaturas_ordenadas)
    invictas.sort(key=lambda c: (c[0], c[1]))

    return invictas, len(invictas)
