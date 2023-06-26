'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

# 80%
def area(p, mapa):
    n = len(mapa)
    if n == 0:
        return 0
    m = len(mapa[0])
    if m == 0:
        return 0

    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = [(p[0], p[1])]
    visited[p[0]][p[1]] = True

    count = 1

    while len(queue) > 0:
        x, y = queue.pop(0)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and mapa[nx][ny] == '.' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count


def main():
    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*...*",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))

if __name__ == '__main__':
    main()


