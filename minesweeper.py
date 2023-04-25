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
   
    variaveis=[]
    for i in range(len(puzz)):
        for j in range(len(puzz[i])):
            varname = "V_{0}_{1}".format(i,j)
            variaveis.append(varname)

    constraints = {}
    dominios = []
    
    vizinhos = {}
    for v in variaveis :
        for x in range(1):
            dominios[v] = [0,1]
                              
    n = len(puzz)
    m = len(puzz[i])
    for i in range(n):
            for j in range(m):
                if puzz[i][j] != -1:  # cell is numbered
                    neighbors = []
                    for x in range(max(0, i-1), min(n, i+2)):
                        for y in range(max(0, j-1), min(m, j+2)):
                            if (x, y) != (i, j):
                                neighbors.append((x, y))
                    problem.addConstraint(ExactSumConstraint(1, neighbors), neighbors)

    # Solve the problem
    solutions = problem.getSolutions()
 
    return CSP(variaveis, dominios, vizinhos,constraints)

def show_domains(doms):
    sd = []
    
    return sd
    