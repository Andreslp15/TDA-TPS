def es_dominante(a,b):
    return a[0] > b[0] and a[1] >= b[1]

def buscar_invictos(v1,v2):
    i = 0
    j = 0
    sol = []
    
    while i < len(v1) and j < len(v2):
        if es_dominante(v1[i],v2[j]):
            j += 1
        elif es_dominante(v2[j],v1[i]):
            i += 1
        else:
            x1,y1 = v1[i]
            x2,y2 = v2[j]
            if x1 > x2 or (x1 == x2 and y1 < y2):
                sol.append(v1[i])
                i += 1
            else:
                sol.append(v2[j])
                j += 1

    sol.extend(v1[i:])
    sol.extend(v2[j:])

    return sol

def criaturas_invictas(v):
    if len(v) <= 1:
        return v,len(v)

    mitad = len(v)//2
    izq = v[:mitad]
    der = v[mitad:]

    sol_izq,_ = criaturas_invictas(izq)
    sol_der,_ = criaturas_invictas(der)

    invictas = buscar_invictos(sol_izq,sol_der)

    return invictas, len(invictas)
