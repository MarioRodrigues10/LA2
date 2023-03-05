'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''
import unittest

# 100%
def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))

def cruzamentos(ruas):
    cruzamentos = []
    for rua in ruas:
        if rua[0] != rua[-1]:
            cruzamentos.append(rua[0])
            cruzamentos.append(rua[-1])
        else:
            cruzamentos.append(rua[0])
    cruzamentos.sort()
    for i in range(len(cruzamentos)):
        cruzamentos[i] = (cruzamentos[i], cruzamentos.count(cruzamentos[i]))
    temp = cruzamentos[0][0]
    for i in range(len(cruzamentos)):
        if cruzamentos[i][0] == temp and i != 0:
            temp = cruzamentos[i][0]
            cruzamentos[i] = ("abc",100)
        else:
            temp = cruzamentos[i][0]
    cruzamentos = [x for x in cruzamentos if x[0] != "abc"]
    cruzamentos.sort(key=lambda x: (x[1], x[0]))
    return cruzamentos




class cruzamentosTest(unittest.TestCase):
    
    def test_cruzamentos_2(self):
        self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])

    def test_cruzamentos_1(self):
        self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])

            

if __name__ == '__main__':
    main()
