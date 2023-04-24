from csp import *
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
    def constraint_gen(grid, row, col):
        """
        Returns a list of neighboring elements of a grid element located at (row, col)
        """
        rows = len(grid)
        cols = len(grid[0])
        neighbors = []
        for i in range(len(puzz)):
            for j in range(len(puzz[0])):
                    if puzz[i][j]!=-1: 
                        # Iterate over adjacent rows
                        for i in range(max(0, row-1), min(rows, row+2)):
                            # Iterate over adjacent columns
                            for j in range(max(0, col-1), min(cols, col+2)):
                                # Skip the center element
                                if i == row and j == col:
                                    continue
                            # Add the adjacent element to the list of neighbors
                            neighbors.append(grid[i][j])
        csp.add_constraint(neighbors, lambda *values: sum(values) == puzz) 
        solution = backtracking_search(csp)
        return neighbors
    def vargenerator(puzz):
        vars = []
        for x in puzz :
            for y in x:
                if y is int:
                    csp.add_variable("V_" + str(puzz.index(x)) + "_" + str(puzz.index(y)))
                    
        return  vars.sort()
    def neighgenerator(puzz):
        neighbours = []
        for x in puzz :
            for y in x:
                if y is int:
                    neighbours.append(get_neighbors(puzz,x,y))
                    
        return  neighbors.sort()
    

    variaveis = list(vargenerator(puzz))
    vizinhos = list(neighgenerator(puzz))
        
    # Definir Domínios
    # Devolve um dicionario com os domínios com as variáveis 
    def domaingen(puzz):
        dominios = {}
        for v in variaveis :
            dominios[v] = [0,1,2,3,4,5,6,7,8,9]
                   
                
        
    return CSP(variaveis, dominios, vizinhos,constraints)
    pass

def show_domains(dom):
    return dom.dominios