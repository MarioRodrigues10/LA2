"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""
import unittest

def formata(codigo):
    novo = []
    novo2 = []
    count = 0
    for i in range(len(codigo)):
        if codigo[i] == ' ':
            count += 1
        else:
            count = 0
        if count < 2:
            novo.append(codigo[i])
    
    print(''.join(novo))
    for i in range(len(novo)):
        if novo[i] == ';':
            novo2.append(novo[i])
            novo2.append('\n')
            novo2.append(' ')
        elif novo[i] == '{':
            novo2.append(novo[i])
            novo2.append('\n')
            novo2.append(' ')
        else:
            novo2.append(novo[i])

        
    junto = ''.join(novo2)
    return junto

class formataTest(unittest.TestCase):

    def test_formata_1(self):
            codigo = "int x;x=0;x=x+1;"
            self.assertEqual(formata(codigo),"int x;\nx=0;\nx=x+1;")

    def test_formata_2(self):
            codigo = "int main() {int x;x=0;     x=x+1;}"
            self.assertEqual(formata(codigo),"int main() {\n  int x;\n  x=0;\n  x=x+1;\n}")
            
#int main() {
#  int x;
#  x=0;
#  x=x+1;
#}
def main():
    print("<h4>formata</h4>")
    codigo = "int main() {int x;x=0;     x=x+1;}"
    print(formata(codigo))
  
if __name__ == '__main__':
    main()
    unittest.main()