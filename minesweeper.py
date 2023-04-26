from csp import *
from p3_aux import *
import csp
"""
V_1_1' = 1
V_2_0' + 'V_2_1' + 'V_1_1' = 2
'V_3_1' + 'V_4_2' + 'V_3_3' + 'V_2_2' + 'V_2_1' = 4
"""
"""fazer uma função que receba A,a, B,b (as maiusculas são as variaveis das células 
e as minusculas os valores que estão lá dentro), 
verifique as contraints e devolva true se não violar nenhuma contraint"""

"""dar isso tudo ao minesweeper_csp = CSP(variables, domains, neighbors, constraints) 
mas deve ser meter num dic ou assim"""

def minesweeper_CSP(puzz):
    #Definir Variáveis
    #definicao dos valores do puzzle são universais
    r = len(puzz)
    c = len(puzz[0])
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]
    variaveis=[]
    for x in range(r):
        for y in range(c):
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and isinstance(puzz[nx][ny], int):
                    varname = "V_{0}_{1}".format(x,y)
                    variaveis.append(varname)
                
    variaveis = set(variaveis)
    variaveis = list(variaveis)
    variaveis.sort()

    constraints = {}
    dominios = {}
    vizinhos = {}
    
    def domain_gen(puzz):
        bomb_positions = set()
        for i in range(r):
            for j in range(c):
                # If the cell is not empty and the number of adjacent bombs is
                # equal to the value in the cell, then all adjacent cells are bombs
                if puzz[i][j] != 0 and puzz[i][j] == count_adjacent_bombs(puzz, i, j):
                    for x, y in get_adjacent_cells(grid, i, j):
                        if puzz[x][y] == -1:
                            bomb_positions.add((x, y))

    domain_gen(puzz)

    def funct(a,A,b,B):
        pass
    def constraint_gen(puzz):
        csp.add_constraint(neighbors, lambda *values: sum(values) == puzz[i][j]) 
        
 
    return CSP(variaveis, dominios, vizinhos,constraints)
