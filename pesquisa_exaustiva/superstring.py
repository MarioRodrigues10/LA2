'''

Implemente um função que calcula a menor string que contém todas as palavras 
recebidas na lista de input. Assuma que todas as palavras são disjuntas entre si, 
ou seja, nunca haverá inputs onde uma das palavras está contida noutra.

'''
import itertools

#80%
def superstring(strings):
    shortest_superstring = None

    # Generate all permutations of the input strings
    for permutation in itertools.permutations(strings):
        # Concatenate the strings in the permutation
        concatenated_string = permutation[0]
        for i in range(1, len(permutation)):
            current_string = permutation[i]
            overlap = len(current_string)
            while overlap > 0:
                if permutation[i-1].endswith(current_string[:overlap]):
                    break
                overlap -= 1
            concatenated_string += current_string[overlap:]

        # Update the shortest superstring if it is None or shorter than the current shortest
        if shortest_superstring is None or len(concatenated_string) < len(shortest_superstring):
            shortest_superstring = concatenated_string

    return shortest_superstring

def main():
    print("<h3>superstring</h3>")
    strings = ['ana','nao','ama']
    print("in:",strings)
    print("out:",superstring(strings))


import unittest

class superstringTest(unittest.TestCase):

    def test_superstring_1(self):
            strings = ['ana','nao','ama']
            self.assertEqual(superstring(strings),'amanao')

    def test_superstring_2(self):
            strings = ['acor','laco','cola']
            self.assertEqual(superstring(strings),'colacor')
          
if __name__ == '__main__':
    main()
    unittest.main()
