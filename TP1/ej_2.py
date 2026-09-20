# Se dice que una criatura C = (x’, y’) domina a otra D = (x, y), C domina a D si y solo si x < x’ e y <= y’. 
# Una criatura que no es dominada por ninguna otra es una invicta, y merece un lugar en el salón de las leyendas. 
# Se pide obtener todas las criaturas invictas.

A = (3,2)
B = (4,2)
C = (2,2)
D = (1,1)
E = (1,3)
F = (2,3)

v = [(3, 4), (1, 5), (4, 2), (2, 2), (5, 1), (4, 5)]
s = ([(4, 2), (4, 5), (5, 1)], 3)

v_1 = [A,C,B,D,E]
v_2 = [D,D,D,D]
v_3 = [A,B,B,E]
v_4 = [A,D,B,D,E,D,F]
v_5 = [D,B,E,D,F]
v_6 = [E,D,A,C,F]

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
            x1 = v1[i][0]
            x2 = v2[j][0]
            if x1 > x2:
                sol.append(v1[i])
                i += 1
            elif x1 == x2:
                y1 = v1[i][1]
                y2 = v2[j][1]
                if y1 >= y2:
                    sol.append(v2[j])
                    j += 1
                else:
                    sol.append(v1[i])
                    i += 1
            else:
                sol.append(v2[j])
                j += 1

    while i < len(v1):
        sol.append(v1[i])
        i += 1

    while j < len(v2):
        sol.append(v2[j])
        j += 1

    return sol

def criaturas_invictas(v):
    if len(v) <= 1:
        return v

    mitad = len(v)//2
    izq = v[:mitad]
    der = v[mitad:]

    sol_izq = criaturas_invictas(izq)
    sol_der = criaturas_invictas(der)

    invictas = buscar_invictos(sol_izq,sol_der)

    return invictas

def criaturas_inv_o_n_2(v):
    n = len(v)
    sol = []

    for i in range(n):
        invicto = True

        for j in range(n):
            if i != j and es_dominante(v[j], v[i]):
                invicto = False
                break

        if invicto:
            sol.append(v[i])
    return sol

def main():
    ejemplos = [v_1,v_2,v_3,v_4,v_5,v_6]
    for b in ejemplos:
        invictas = criaturas_inv_o_n_2(b)
        print((invictas,len(invictas)))
   
    print("")

    for a in ejemplos:
        invictas = criaturas_invictas(a)
        print((invictas,len(invictas)))

main()