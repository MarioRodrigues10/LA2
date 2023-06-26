"""

Defina uma função que calcula a área de uma figura desenhada com pecas
lineares. A função recebe uma lista de pecas, onde para cada peça se indica
a sua localização no plano, a orientação (True significa horizontal e False
vertical), e a dimensão.

"""

def area(pecas):
    coordh = []
    coordv = []

    for i in pecas:
        for j in range(i[3]):
            quadrados = []
            if (i[2]):
                quadrados += (i[0]+j,i[1]),(i[0]+j,i[1]+1),(i[0]+j+1,i[1]),(i[0]+j+1,i[1]+1)
                quadrados.sort()
                coordh.append(quadrados)
            else:
                quadrados += (i[0], i[1] +j), (i[0]+1, i[1]+j), (i[0], i[1]+j+1), (i[0]+1 , i[1] +j+1)
                quadrados.sort()
                coordv.append(quadrados)

    area = 0
    for i in pecas:
        area += i[3]

    for i in coordv:
        if i in coordh:
            area-=1
    return area


def main():
    print("<h4>area</h4>")
    pecas = [(0,1,True,3),(1,0,False,3)]
    print(area(pecas))
    
if __name__ == '__main__':
    main()
