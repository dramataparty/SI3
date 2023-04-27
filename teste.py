from csp import CSP

def minesweeper_CSP(puzz):
    # Definir Variáveis
    # definicao dos valores do puzzle são universais
    r = len(puzz)
    c = len(puzz[0])
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]
    variaveis=[]
    vizinhos = {}
    for x in range(r):
        for y in range(c):
            vizs = []
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                varname = "V_{0}_{1}".format(x,y)
                if 0 <= nx < r and 0 <= ny < c and isinstance(puzz[nx][ny], int):
                    variaveis.append(varname)
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                vizname = "V_{0}_{1}".format(nx,ny)
                if 0 <= nx < r and 0 <= ny < c and not isinstance(puzz[nx][ny], int) and vizname not in vizs:
                    vizs.append(vizname)
            vizinhos[varname] = sorted(vizs)
            vizinhos.update({varname:set(vizs)})

    variaveis = sorted(set(variaveis))

    def minesweeper_constraint(a, A, b, B):
        return A != B

    constraints = []
    for var in vizinhos:
        for viz in vizinhos[var]:
            constraints.append((var, viz, minesweeper_constraint))

    dominios = {}
    for var in variaveis:
        dominios[var] = {0, 1}

    def funct(a, A, b, B):
        pass

    return CSP(variaveis, dominios, vizinhos, constraints)


try:
    puzzle = [[1, 2, '#', '#', '#'],
              [1, '#', '#', '#', 2],
              ['#', '#', '#', 4, '#'],
              ['#', '#', 2, '#', 3],
              [2, 2, '#', 2, '#']]
    xxx = minesweeper_CSP(puzzle)
    grafo = xxx.neighbors
    print(sorted([(var, sorted(val)) for (var, val) in grafo.items()]))
except Exception as e:
    print(repr(e))
