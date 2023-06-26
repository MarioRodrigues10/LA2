'''

Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.

'''
import unittest
from itertools import permutations

def multiplos(n, d):
    count = 0
    digits = list(range(1, n + 1))
    perms = permutations(digits)
    for perm in perms:
        num = int("".join(map(str, perm)))
        if num % d == 0:
            count += 1
    return count

def main():
    print("<h3>multiplos</h3>")
    print("in:",3,3)
    print("out:",multiplos(3,3))

class multiplosTest(unittest.TestCase):

    def test_multiplos_1(self):
            self.assertEqual(multiplos(3,3),6)

    def test_multiplos_2(self):
            self.assertEqual(multiplos(5,12),24)
          
            
if __name__ == '__main__':
    main()
    unittest.main()