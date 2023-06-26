'''

Um ciclo Hamiltoniano num grafo não orientado é um caminho no grafo que passa
uma e uma só vez por cada nó e termina no nó onde começou.

Implemente uma função que calcula o menor (em ordem lexicográfica) ciclo 
Hamiltoniano de um grafo, caso exista. Se não existir deve devolver None.

'''
import unittest

# 90%
def hamilton(arestas):
    return []

def main():
    print("<h3>hamilton</h3>")
    arestas = [(1,3),(1,4),(2,4),(3,4),(0,1),(1,2),(0,3)]
    print("in:",arestas)
    print("out:",hamilton(arestas))

class hamiltonTest(unittest.TestCase):

    def test_hamilton_1(self):
            arestas = [(0,1),(1,2),(0,3),(1,3),(1,4),(2,4),(3,4)]
            self.assertEqual(hamilton(arestas),[0,1,2,4,3])
            
    def test_hamilton_2(self):
            arestas = [(0,1),(1,2),(0,3),(1,3),(1,4),(2,4)]
            self.assertEqual(hamilton(arestas),None)
          
            
if __name__ == '__main__':
    main()
    unittest.main()