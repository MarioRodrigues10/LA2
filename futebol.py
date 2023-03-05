'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''
# 100%
def tabela(jogos):
    lista = []
    difGolos = []
    for i in range(len(jogos)):
        if jogos[i][1] > jogos[i][3]:
            existe(jogos[i][0], lista, 3)
            difGolosEq(jogos[i][0], difGolos, jogos[i][1] - jogos[i][3])
            difGolosEq(jogos[i][2], difGolos, jogos[i][3] - jogos[i][1])
        elif jogos[i][1] < jogos[i][3]:
            existe(jogos[i][2], lista, 3)
            difGolosEq(jogos[i][0], difGolos, jogos[i][1] - jogos[i][3])
            difGolosEq(jogos[i][2], difGolos, jogos[i][3] - jogos[i][1])
        else:
            existe(jogos[i][0], lista, 1)
            existe(jogos[i][2], lista, 1)
            difGolosEq(jogos[i][0], difGolos, 0)
            difGolosEq(jogos[i][2], difGolos, 0)

    temp = []
    # CREATE  A LIST WITH (TEAM, POINTS, DIF GOALS)
    for i in range(len(lista)):
        for j in range(len(difGolos)):
            if lista[i][0] == difGolos[j][0]:
                temp.append((lista[i][0], lista[i][1], difGolos[j][1]))


    # CREATE A SORT BY (FIRST POINTS THEN DIF GOALS)
    temp.sort(key=lambda x: (x[1], x[2]), reverse=True)

    # SORT BY NAME IF POINTS AND DIF GOALS EQUAL BETWEEN 2 TEAMS
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i][1] == temp[j][1] and temp[i][2] == temp[j][2]:
                if temp[i][0] > temp[j][0]:
                    temp[i], temp[j] = temp[j], temp[i]
    for i in range(len(temp)):
        lista[i] = (temp[i][0], temp[i][1])
    

    return lista

def existe(equipa, lista, qnt):
    for i in range(len(lista)):
        if lista[i][0] == equipa:
            lista[i] = (lista[i][0], lista[i][1] + qnt)
            return True
    lista.append((equipa, qnt))
    return False

def difGolosEq(equipa, lista, qnt):
    for i in range(len(lista)):
        if lista[i][0] == equipa:
            lista[i] = (lista[i][0], lista[i][1] + qnt)
            return True
    lista.append((equipa, qnt))
    return False

def main():
    print("<h3>tabela</h3>")
    jogos =  [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2), ("Boavista",0,"Porto",0), ("Boavista",0,"Benfica",0)]
    print("in:",jogos)
    print("out:",tabela(jogos))


import unittest

class tabelaTest(unittest.TestCase):

    def test_tabela_1(self):
            jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
            self.assertEqual(tabela(jogos),[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])

    def test_tabela_2(self):
            jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2), ("Boavista",0,"Porto",0), ("Boavista",0,"Benfica",0)]
            self.assertEqual(tabela(jogos),[('Benfica', 4), ('Porto', 4), ('Boavista', 2), ('Sporting', 2)])
            
if __name__ == '__main__':
    main()
