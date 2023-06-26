'''

Um anel de tamanho n (um número par) consiste numa permutação do números de 1 
até n em que a soma de quaisquer dois números adjacentes é um número primo
(considera-se que o primeiro elemento da sequência é adjacente do último).
Implemente uma função que calcule um destes aneis de tamanho n.

'''

import unittest
from itertools import permutations

# 60%
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def anel(n):
    if n == 0: 
        return []
    numbers = list(range(1, n + 1))
    for perm in permutations(numbers):
        if all(is_prime(perm[i] + perm[(i + 1) % n]) for i in range(n)):
            return list(perm)
    return []

def main():
    print("<h3>anel</h3>")
    print("in:",4)
    print("out:",anel(4))

class anelTest(unittest.TestCase):

    def test_anel_1(self):
            self.assertIn(anel(4),[[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]])
            
    def test_anel_2(self):
            self.assertIn(anel(2),[[1,2],[2,1]])
          
            
if __name__ == '__main__':
    main()
    unittest.main()
