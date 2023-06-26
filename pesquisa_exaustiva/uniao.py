'''

Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.

'''

import itertools
# 20%
def uniao(sets):
    # Generate all permutations of the sets
    set_permutations = itertools.permutations(sets)

    # Iterate through each permutation
    for perm in set_permutations:
        # Check if the union of the current permutation is identical to the union of all sets
        if set.union(*perm) == set.union(*sets):
            # Return the minimum number of sets in the permutation
            return len(perm)

    # If no permutation satisfies the condition, return -1
    return -1


def main():
    print("<h3>uniao</h3>")
    sets = [{1,2,3},{2,4},{3,4},{4,5}]
    print("in:",sets)
    print("out:",uniao(sets))


import unittest

class unionTest(unittest.TestCase):

    def test_union_1(self):
            sets = [{1,2,3},{2,4},{3,4},{4,5}]
            self.assertEqual(uniao(sets),2)

    def test_union_2(self):
            sets = [{1},{2},{3,4},{5,6,7,8},{1,3,5,7},{2,4,6,8},{9}]
            self.assertEqual(uniao(sets),3)
          
            
if __name__ == '__main__':
    main()
    unittest.main()