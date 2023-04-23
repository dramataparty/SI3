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
    def vargenerator(puzz):
        vars = []
        for x in puzz :
            for y in x:
                if y is int:
                    vars.append("V_" + str(puzz.index(x)) + "_" + str(puzz.index(y)))
                    
        return  vars.sort()

    variaveis = list(vargenerator(puzz))
        
    # Definir Domínios
    # Devolve um dicionario com os domínios com as variáveis 
    dominios_ABCdifs = {}
    for v in variaveis :
        dominios[v] = [1,2,3]
    
    #Definir Vizinhos
    #Cria o grafo de restrições com os arcos seguintes:
    #A : B
    #B : C
    
    vizinhos = parse_neighbors('A : B C; B: C')

        
    return CSP(variaveis, dominios, vizinhos,different_values_constraint)
    pass

def show_domains(dom):
    return dom.dominios