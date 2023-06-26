"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""

import unittest

#50%
def validas(soma, listas):
    result = []
    for lista in listas:
        if any(sum(sublista) == soma for sublista in subsequences(lista)):
            result.append(lista)
    return result

def subsequences(lista):
    n = len(lista)
    result = []
    for i in range(1, 2 ** n):
        subsequence = [lista[j] for j in range(n) if (i >> j) & 1]
        result.append(subsequence)
    return result

def main():
    print("<h3>validas</h3>")
    listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
    print("in:",10,listas)
    print("out:",validas(10,listas))

class validasTest(unittest.TestCase):
    
    def test_validas_1(self):
            listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
            self.assertEqual(validas(10,listas),[[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]])

    def test_validas_2(self):
            listas = [[1,1,1,1,1],[2],[3,3,3,3,3,3,3],[4],[5,5,5,5,5]]
            self.assertEqual(validas(5,listas),[[1,1,1,1,1],[5,5,5,5,5]])
          
            
if __name__ == '__main__':
    main()
    #unittest.main()