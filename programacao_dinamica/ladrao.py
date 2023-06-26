"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""
import unittest

#100%
def ladrao(capacidade, objectos):
    n = len(objectos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        nome, valor, peso = objectos[i - 1]
        for j in range(1, capacidade + 1):
            if peso <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - peso] + valor)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacidade]



def main():
    print("<h3>ladrao</h3>")
    objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
    print("in:",10,objectos)
    print("out:",ladrao(10,objectos))
    

class ladraoTest(unittest.TestCase):

    def test_ladrao_1(self):
            objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
            self.assertEqual(ladrao(10,objectos),46)

    def test_ladrao_2(self):
            objectos = [('A',10,1),('B',20,1),('C',30,1),('D',40,1),('E',50,1),('F',60,1),('G',70,1),('H',80,1),('I',90,1),('J',100,1)]
            self.assertEqual(ladrao(10,objectos),550)
           
            
if __name__ == '__main__':
    main()
    unittest.main()