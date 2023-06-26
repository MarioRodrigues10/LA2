'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
 
from collections import defaultdict
import heapq

def tamanho(ruas):
    graph = defaultdict(list)
    for rua in ruas:
        src, dest = rua[0], rua[-1]
        weight = len(rua)
        graph[src].append((dest, weight))
        graph[dest].append((src, weight))

    def dijkstra(graph, start):
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        heap = [(0, start)]
        visited = set()
        while heap:
            (dist, node) = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in graph[node]:
                alt = dist + weight
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    heapq.heappush(heap, (alt, neighbor))
        return distances

    max_distance = -1
    for node in graph.keys():
        distances = dijkstra(graph, node)
        max_distance = max(max_distance, max(distances.values()))

    return max_distance


def main():
    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))

if __name__ == '__main__':
    main()
