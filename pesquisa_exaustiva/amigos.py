'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.

'''

import unittest

def amigos(conhecidos):
    grafo = {}
    for pessoa1, pessoa2 in conhecidos:
        if pessoa1 not in grafo:
            grafo[pessoa1] = set()
        if pessoa2 not in grafo:
            grafo[pessoa2] = set()
        grafo[pessoa1].add(pessoa2)
        grafo[pessoa2].add(pessoa1)

    max_contagem = 0
    visitados = set()
    for pessoa in grafo:
        if pessoa not in visitados:
            contagem = dfs(pessoa, grafo, visitados)
            max_contagem = max(max_contagem, contagem)

    return max_contagem


def dfs(pessoa, grafo, visitados):
    visitados.add(pessoa)
    contagem = 1
    for amigo in grafo[pessoa]:
        if amigo not in visitados:
            contagem += dfs(amigo, grafo, visitados)
    return contagem

def main():
    print("<h3>amigos</h3>")
    conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
    print("in:",conhecidos)
    print("out:",amigos(conhecidos))

class amigosTest(unittest.TestCase):

    def test_amigos_1(self):
            conhecidos = {('pedro','maria'),('pedro','jose'),('pedro','manuel'),('maria','jose'),('maria','francisca'),('jose','francisca'),('francisca','manuel')}
            self.assertEqual(amigos(conhecidos),3)
            
    def test_amigos_2(self):
            conhecidos = {('pedro','maria'),('jose','francisca'),('manuel','pedro')}
            self.assertEqual(amigos(conhecidos),2)
          
            
if __name__ == '__main__':
    main()
    unittest.main()
