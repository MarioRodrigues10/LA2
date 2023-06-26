"""

Implemente uma função que dada uma palavra secreta e uma palavra tentativa
devolva uma lista com os caracteres da palavra tentativa que aparecem na
palavra secreta.
Mais concretamente, para cada caracter que apareça na palavra tentativa
deve também ser indicada a respectiva posição e um booleano que indica se
aparece na mesma posição na palavra secreta ou numa posição diferente.

"""

def count(lista,char):
    num = 0
    for i in lista:
        if (i[0] == char):
            num += 1
    return num

def wordle(secreta,tentativa):
    lista = []
    for i in range(len(tentativa)):
        if not i+1 > len(secreta):
            if tentativa[i] in secreta:
                if count(lista,tentativa[i]) < secreta.count(tentativa[i]):
                    if tentativa[i] == secreta[i]:
                        lista += [(tentativa[i],i,True)]                        
                    else:
                        lista += [(tentativa[i],i,False)]
        else:
            break
    return lista

def main():
    print("<h4>wordle</h4>")
    print(wordle("aba","aa"))
    

if __name__ == '__main__':
    main()