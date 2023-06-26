'''

Implemente uma função que calcula o número mínimo de nós de um grafo 
não orientado que cobrem todas as arestas, ou seja, o tamanho do menor 
conjunto de nós que contém pelo menos um extremo de cada aresta. 
A função recebe a lista de todas as arestas do grafo, sendo cada aresta um 
par de nós.

'''
import unittest


def cobertura(arestas):
    nodes = set()
    for aresta in arestas:
        nodes.add(aresta[0])
        nodes.add(aresta[1])
    return len(nodes) // 2

def main():
    print("<h3>cobertura</h3>")
    arestas = [('portugal','espanha'),('espanha','franca'),('franca','alemanha'),('alemanha','belgica'),('belgica','franca'),('usa','canada'),('usa','mexico'),('marrocos','argelia'),('argelia','libia'),('argelia','mali')]
    print("in:",arestas)
    print("out:",cobertura(arestas))

class coberturaTest(unittest.TestCase):

    def test_cobertura_1(self):
            arestas = [('portugal','espanha'),('espanha','franca'),('franca','alemanha'),('alemanha','belgica'),('belgica','franca'),('usa','canada'),('usa','mexico'),('marrocos','argelia'),('argelia','libia'),('argelia','mali')]
            self.assertEqual(cobertura(arestas),5)

    def test_cobertura_2(self):
            arestas = [('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),('g','h')]
            self.assertEqual(cobertura(arestas),4)
          
            
if __name__ == '__main__':
    main()
    unittest.main()