def minima_molestia(pergaminos):

    pergaminos_ordenados = sorted(pergaminos, key=lambda x: x[0] / x[1], reverse=True)
    C = 0
    molestia = 0

    for wi, ti, ai in pergaminos_ordenados:
        C += ti
        molestia += wi * (C + ai)

    return pergaminos_ordenados