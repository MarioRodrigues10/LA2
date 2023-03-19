'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def maior(vizinhos):
    # create a dictionary to map each country to its neighbors
    adj_list = {}
    for fronteira in vizinhos:
        for i, pais in enumerate(fronteira):
            if pais not in adj_list:
                adj_list[pais] = set()
            adj_list[pais].update(fronteira[:i] + fronteira[i+1:])
    
    # explore the graph using depth-first search
    visited = set()
    max_size = 0
    for pais in adj_list:
        if pais not in visited:
            size = dfs(adj_list, pais, visited)
            max_size = max(max_size, size)
    
    return max_size

def dfs(adj_list, pais, visited):
    visited.add(pais)
    size = 1
    for neighbor in adj_list[pais]:
        if neighbor not in visited:
            size += dfs(adj_list, neighbor, visited)
    return size

def main():
    print("<h3>maior</h3>")
    vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
    print("in:", vizinhos)
    print("out:", maior(vizinhos))

if __name__ == '__main__':
    main()