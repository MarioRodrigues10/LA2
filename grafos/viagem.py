'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''
import heapq
def viagem(rotas, o, d):
    routes = {}
    for r in rotas:
        for i in range(len(r) - 2):
            origin, cost, dest = r[i], r[i + 1], r[i + 2]
            if (origin, dest) in routes:
                routes[(origin, dest)] = min(routes[(origin, dest)], cost)
            else:
                routes[(origin, dest)] = cost

    q = [(0, o)]
    visited = set()
    while q:
        cost, node = heapq.heappop(q)
        if node == d:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor in [n for n in routes if node in n]:
                n = neighbor[1] if neighbor[0] == node else neighbor[0]
                c = cost + routes[neighbor]
                heapq.heappush(q, (c, n))

    return -1


def main():
    print("<h3>viagem</h3>")
    rotas = [["Porto",20,"Lisboa"],
             ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
             ["Braga",3,"Famalicao",3,"Porto"],
             ["Viana",4,"Povoa",3,"Porto"],
             ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
            ]
    print("in: Caminha Lisboa")
    print('\n'.join(map(str,rotas)))
    print("out:",viagem(rotas,"Caminha","Lisboa"))
    