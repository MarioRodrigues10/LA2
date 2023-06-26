'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

import collections
#100%
def frequencia(texto):
    lista = texto.split()
    lista.sort()
    lista = collections.Counter(lista).most_common()
    print(lista)
    lista = sorted(lista, key=lambda x: (-x[1], x[0]))
    lista = [x[0] for x in lista]
    return lista

def main():
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto))


import unittest

class frequenciaTest(unittest.TestCase):
    
    def test_frequencia_1(self):
            self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])

    def test_frequencia_2(self):
            self.assertEqual(frequencia("ola"),['ola'])

if __name__ == '__main__':
    main()
    #unittest.main()