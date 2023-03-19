'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

# 40%
def travessia(mapa):
    nrows, ncols = len(mapa), len(mapa[0])
    INF = float('inf')

    # Compute the minimum cost of crossing the region
    dp = [[INF] * ncols for _ in range(nrows)]
    for j in range(ncols):
        dp[0][j] = 0

    for i in range(1, nrows):
        for j in range(ncols):
            for dj, di in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nj, ni = j + dj, i + di
                if 0 <= nj < ncols and 0 <= ni < nrows:
                    diff = abs(int(mapa[i][j]) - int(mapa[ni][nj]))
                    if diff <= 2:
                        cost = diff + 1
                        dp[i][j] = min(dp[i][j], dp[ni][nj] + cost)

    # Find the minimum cost starting position
    min_cost = INF
    start_col = -1
    for j in range(ncols):
        if dp[nrows-1][j] < min_cost:
            min_cost = dp[nrows-1][j]
            start_col = j
        elif dp[nrows-1][j] == min_cost and j < start_col:
            start_col = j

    return (start_col, min_cost)


def main():
    print("<h3>travessia</h3>")
    mapa = ["4563",
            "9254",
            "7234",
            "3231",
            "3881"]
    print("in:")
    print('\n'.join(mapa))
    print("out:",travessia(mapa))
    
    
if __name__ == '__main__':
    main()
