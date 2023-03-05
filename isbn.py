'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''
import unittest

#100%
def isbn(livros):
    flag1 = 1
    invalid = []

    for livro in livros.items():
        r = 0
        for number in livro[1][:-1]:
            if flag1 == 1:
                r += 1* int(number,10)
                flag1 = 0
            else:
                r += 3* int(number,10)
                flag1 = 1
            
        r += int(livro[1][-1],10)
                
        if(r % 10 != 0):
            invalid.append(livro[0])
            
    invalid.sort()
    return invalid


def main():
    print("<h3>isbn</h3>")
    livros = {
        "Todos os nomes":"9789720047572",
        "Ensaio sobre a cegueira":"9789896604011",
        "Memorial do convent":"9789720046711",
        "Os cus de Judas":"9789722036757"
    }
    print("in:",livros)
    print("out:",isbn(livros))

class isbnTest(unittest.TestCase):
    
    def test_isbn_1(self):
            livros = {
                "Todos os nomes":"9789720047572",
                "Ensaio sobre a cegueira":"9789896604011",
                "Memorial do convento":"9789720046711",
                "Os cus de Judas":"9789722036757"
            }
            self.assertEqual(isbn(livros),["Memorial do convento","Todos os nomes"])

    def test_isbn_2(self):
            livros = {
                "Ola mundo":"0000000000001"
            }
            self.assertEqual(isbn(livros),["Ola mundo"])


if __name__ == '__main__':
    main()
    unittest.main()