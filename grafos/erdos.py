'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''

def erdos(artigos, n):
    coautores = {}
    for artigo, autores in artigos.items():
        for autor in autores:
            if autor not in coautores:
                coautores[autor] = set()
            coautores[autor].add(artigo)
    
    queue = ["Paul Erdos"]
    visited = set(queue)
    dist = {"Paul Erdos": 0}
    while queue:
        atual = queue.pop(0)
        if dist[atual] >= n:
            break
        for artigo in coautores.get(atual, set()):
            for autor in artigos[artigo]:
                if autor not in visited:
                    dist[autor] = dist[atual] + 1
                    visited.add(autor)
                    queue.append(autor)
    
    dist = sorted(dist.items(), key=lambda x: (x[1], x[0]))
    dist = [x[0] for x in dist]
    return dist


def main():
    print("<h3>erdos</h3>")
    artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
               "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
               "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
              }
    print("in: 2")
    print('\n'.join(map(str,artigos.items())))
    print("out:",erdos(artigos,2))

if __name__ == '__main__':
    main()
