import unittest
'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

# 100%
def apelidos(nomes):
    nomes.sort(key=lambda x: (len(x.split())-1, x))
    return nomes


def main():
    nomes = ['João da Silva', 'Maria da Silva', 'João da Silva Santos', 'João de Sousa', 'Maria de Souza']
    print(apelidos(nomes))


class apelidosTest(unittest.TestCase):
    
    def test_apelidos_1(self):
        self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])

    def test_apelidos_2(self):
        self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])

            
if __name__ == '__main__':
    unittest.main()
