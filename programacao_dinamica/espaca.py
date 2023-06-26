"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
import unittest

#80%
def espaca(frase, palavras):
    n = len(frase)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and frase[j:i] in palavras:
                dp[i] = True
                break

    if not dp[n]:
        return ""

    reconstructed = []
    i = n
    while i > 0:
        for j in range(i):
            if dp[j] and frase[j:i] in palavras:
                reconstructed.append(frase[j:i])
                i = j
                break

    return " ".join(reconstructed[::-1])

def main():
    print("<h3>espaca</h3>")
    palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
    print("in:","estecursoeomaior",palavras)
    print("out:",espaca("estecursoeomaior",palavras))
    
import unittest

class espacaTest(unittest.TestCase):
    
    def test_espaca_1(self):
            palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
            self.assertEqual(espaca("estecursoeomaior",palavras),"este curso e o maior")
        
    def test_espaca_2(self):
            palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
            self.assertEqual(espaca("ogatomiaeavacamuge",palavras),"o gato mia e a vaca muge")
           
            
if __name__ == '__main__':
    main()
    unittest.main()
