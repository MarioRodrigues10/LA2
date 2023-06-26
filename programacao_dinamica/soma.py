"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""

import unittest

#100%
def maxsoma(lista):
    max_sum = float('-inf')
    current_sum = 0

    for num in lista:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum



def main():
    print("<h3>maxsoma</h3>")
    lista = [-2,1,-3,4,-1,2,1,-5,4]
    print("in:",lista)
    print("out:",maxsoma(lista))


class somaTest(unittest.TestCase):
    
    def test_maxsoma_1(self):
            lista = [-2,1,-3,4,-1,2,1,-5,4]
            self.assertEqual(maxsoma(lista),6)

    def test_maxsoma_2(self):
            lista = [1,2,3,4,-11,1,2,3,4,5]
            self.assertEqual(maxsoma(lista),15)
          
            
if __name__ == '__main__':
    main()
    unittest.main()