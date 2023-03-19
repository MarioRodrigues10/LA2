'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''
#60%
def caminho(mapa):
    start = (0, 0)
    end = (len(mapa) - 1, len(mapa[0]) - 1)
    
    def dfs(curr, visited, path):
        if curr == end:
            return path
        
        row, col = curr
        for drow, dcol, direction in [(1, 0, "S"), (-1, 0, "N"), (0, 1, "E"), (0, -1, "O")]:
            next_row, next_col = row + drow, col + dcol
            if (
                0 <= next_row < len(mapa)
                and 0 <= next_col < len(mapa[0])
                and mapa[next_row][next_col] != "#"
                and (next_row, next_col) not in visited
            ):
                visited.add((next_row, next_col))
                result = dfs((next_row, next_col), visited, path + direction)
                if result:
                    return result
                visited.remove((next_row, next_col))
        
        return None
    
    visited = set()
    visited.add(start)
    return dfs(start, visited, "")


def main():
    print("<h3>caminho</h3>")
    mapa = ["  ########",
            "# # #    #",
            "# # #### #",
            "# #      #",
            "# # # ####",
            "# # #    #",
            "#   # #  #",
            "##### ####",
            "#        #",
            "########  "]
    print("in:")
    print('\n'.join(mapa))
    print("out:",caminho(mapa))
    

            