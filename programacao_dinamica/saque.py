"""

Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

"""

import unittest

#60%
def saque(mapa):
    rows = len(mapa)
    cols = len(mapa[0])

    dp = [[0] * cols for _ in range(rows)]

    # Fill the first row
    for j in range(cols):
        if mapa[0][j].isnumeric():
            dp[0][j] = int(mapa[0][j])
        elif j > 0:
            dp[0][j] = dp[0][j - 1]

    # Fill the first column
    for i in range(rows):
        if mapa[i][0].isnumeric():
            dp[i][0] = int(mapa[i][0])
        elif i > 0:
            dp[i][0] = dp[i - 1][0]

    # Fill the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if mapa[i][j] == '#':
                continue
            if mapa[i][j].isnumeric():
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + int(mapa[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]


def main():
    print("<h3>saque</h3>")
    mapa = [".3......",
            "........",
            "...5#...",
            "...##...",
            ".....9..",
            "..2.....",
            "..2.....",
            "..2....."]
    print("in:")
    print('\n'.join(mapa))
    print("out:",saque(mapa))


class saqueTest(unittest.TestCase):
    
    def test_saque_1(self):
            mapa = [".3......",
                    "........",
                    "...5#...",
                    "...##...",
                    ".....9..",
                    "..2.....",
                    "..2.....",
                    "..2....."]
            self.assertEqual(saque(mapa),12)
        
    def test_saque_2(self):
            mapa = ["11111",
                    "0###1",
                    "0###1",
                    "0###1",
                    "00001"]
            self.assertEqual(saque(mapa),9)
          
            
if __name__ == '__main__':
    main()
    unittest.main()
