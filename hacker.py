"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""
import unittest


def hacker(log):
    log.sort(key=lambda x: x[1])
    cartao_temp = (log[0][0], log[0][1])
    cartao_final = []
    temp = log[0][1]
    print(temp)
    for i in range(0, len(log)):
        if log[i][1] == temp:
            cartao_temp = (cartao_temp[0], cartao_temp[1])
            cartao_temp = (cartao_temp[0], log[i][1])
            for j in range(len(log[i][0])):
                if log[i][0][j] != "*":
                    print(log[i][0][j])
                    cartao_temp = (cartao_temp[0][:j] + log[i][0][j] + cartao_temp[0][j + 1:], cartao_temp[1])
            cartao_final.append(cartao_temp)
        else:
            cartao_final.append(cartao_temp)                                                                        
            cartao_temp = (log[i][0], log[i][1])
            temp = log[i][1]
            for j in range(len(log[i][0])):
                if log[i][0][j] != "*":
                    cartao_temp = (cartao_temp[0][:j] + log[i][0][j] + cartao_temp[0][j + 1:], cartao_temp[1])

    cartao_final.append(cartao_temp)
    cartao_final.sort(key=lambda x: (x[0].count("*"), x[1]))
    cartao_final = list(dict.fromkeys(cartao_final))
            
    return cartao_final


def main():
    print("<h3>hacker</h3>")
    log =[("0000***********", "ze@gmail.com"),
               ("****1234********", "maria@mail.pt")]
    print("in:", log)
    print("out:", hacker(log))


class hackerTest(unittest.TestCase):
    
    def test_hacker_1(self):
            log = [("****1234********","maria@mail.pt"),
                   ("0000************","ze@gmail.com"),
                   ("****1111****3333","ze@gmail.com")]
            self.assertEqual(hacker(log),[("00001111****3333","ze@gmail.com"),("****1234********","maria@mail.pt")])       

    def test_hacker_2(self):
            log = [("0000************","ze@gmail.com"),
                   ("****1234********","maria@mail.pt")]
            self.assertEqual(hacker(log),[("****1234********","maria@mail.pt"),("0000************","ze@gmail.com")])  
            

if __name__ == '__main__':
    main()
