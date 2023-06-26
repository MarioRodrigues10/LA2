'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

'''
import unittest

def sacos(peso, compras):
    compras.sort(reverse=True) 

    bags = 0
    current_weight = 0

    for item in compras:
        if current_weight + item <= peso:
            current_weight += item
        else:
            bags += 1
            current_weight = item

    if current_weight > 0:
        bags += 1

    return bags


def main():
    print("<h3>sacos</h3>")
    compras = [3,6,2,1,5,7,2,4,1]
    print("in:",10,compras)
    print("out:",sacos(10,compras))

import unittest

class sacosTest(unittest.TestCase):

    def test_sacos_1(self):
            compras = [3,6,2,1,5,7,2,4,1]
            self.assertEqual(sacos(10,compras),4)

    def test_sacos_2(self):
            compras = [3,3,3,3,5,5,11]
            self.assertEqual(sacos(11,compras),3) 
          
            
if __name__ == '__main__':
    main()
    unittest.main()