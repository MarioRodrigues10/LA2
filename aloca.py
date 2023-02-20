import unittest
import collections
def main():
    prefs = {10885: [1, 5], 40000: [5], 10000: [1, 2]}
    print("in:", prefs)
    print("out:", aloca(prefs))


def aloca(prefs):
    sort_dictionary = collections.OrderedDict(sorted(prefs.items()))
    for num in sort_dictionary.copy():
        if sort_dictionary[num]:
            temp = int(sort_dictionary[num][0])
            sort_dictionary.update({num: sort_dictionary[num][0]})
            sort_dictionary.pop(num)
            for null in sort_dictionary.copy():
                if temp in sort_dictionary[null]:
                    sort_dictionary[null].remove(temp)
    if not sort_dictionary:
        return []
    else:
        return list(sort_dictionary)


class Teste(unittest.TestCase):
    def teste(self):
        prefs = {10885: [1, 5], 40000: [5], 10000: [1, 2]}
        self.assertEqual(aloca(prefs), [40000])

    def test_aloca_2(self):
        prefs = {30000: [1], 20000: [2], 10000: [3]}
        self.assertEqual(aloca(prefs), [])


if __name__ == '__main__':
    main()
    unittest.main()
