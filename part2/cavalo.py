'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''
import heapq
def saltos(o, d):
    # matriz de visitados
    visited = {}

    # fila de busca
    queue = [(0, o[0], o[1])]
    visited[(o[0], o[1])] = True

    while len(queue) > 0:
        dist, x, y = heapq.heappop(queue)

        # se chegámos ao destino, devolver o número de saltos
        if x == d[0] and y == d[1]:
            return dist

        # verificação das células vizinhas
        for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            nx = x + dx
            ny = y + dy

            # se a célula vizinha não estiver visitada, adicioná-la à fila de busca
            if (nx, ny) not in visited:
                heapq.heappush(queue, (dist + 1, nx, ny))
                visited[(nx, ny)] = True

    return -1


def main():
    print("<h3>saltos</h3>")
    print("in: (0,0) (1,1)")
    print("out:",saltos((0,0),(1,1)))

if __name__ == '__main__':
    main()

