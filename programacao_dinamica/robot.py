"""

Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partido num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""
import unittest

# 40%
def probabilidade(passos, probs):
    directions = ['U', 'D', 'L', 'R']
    dp = [[0] * (2 * passos + 1) for _ in range(passos + 1)]

    dp[0][passos] = 1

    for i in range(1, passos + 1):
        for j in range(2 * passos + 1):
            for direction in directions:
                prob = probs[direction]
                if direction == 'U' and j - 1 >= 0:
                    dp[i][j] += prob * dp[i - 1][j - 1]
                elif direction == 'D' and j + 1 < 2 * passos + 1:
                    dp[i][j] += prob * dp[i - 1][j + 1]
                elif direction == 'L' and j - 1 >= 0:
                    dp[i][j] += prob * dp[i - 1][j - 1]
                elif direction == 'R' and j + 1 < 2 * passos + 1:
                    dp[i][j] += prob * dp[i - 1][j + 1]
                elif direction == 'L' and j == 0:
                    dp[i][j] += prob * dp[i - 1][j]
                elif direction == 'R' and j == 2 * passos:
                    dp[i][j] += prob * dp[i - 1][j]

    return round(dp[passos][passos], 2)

def main():
    print("<h3>probabilidade</h3>")
    probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
    print("in:",2,probs)
    print("out:",probabilidade(2,probs))


class robotTest(unittest.TestCase):

    def test_probabilidade_1(self):
            probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
            self.assertEqual(probabilidade(2,probs),0.25)
        
    def test_probabilidade_2(self):
            probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
            self.assertEqual(probabilidade(6,probs),0.08)
          
            
if __name__ == '__main__':
    main()
    unittest.main()
