"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

import unittest

# 70% 
def crescente(lista): 
    if not lista:
        return 0
    
    n = len(lista)
    dp = [1] * n  # Inicializamos uma lista de comprimentos de subsequência com 1
    
    for i in range(1, n):
        for j in range(i):
            if lista[i] > lista[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    print("<h3>crescente</h3>")
    lista = [5,2,7,4,3,8]
    print("in:",lista)
    print("out:",crescente(lista))
    
class crescenteTest(unittest.TestCase):
    
    def test_crescente_1(self):
            lista = [5,2,7,4,3,8]
            self.assertEqual(crescente(lista),3)

    def test_crescente_2(self):
            lista = [15,27,14,38,26,55,46,65,85]
            self.assertEqual(crescente(lista),6)
            
            
if __name__ == '__main__':
    unittest.main()
