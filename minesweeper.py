from csp import CSP
import itertools
from collections import defaultdict


def minesweeper_CSP(puzz):
    r = len(puzz)
    c = len(puzz[0])
    offsets = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    variaveis=[]
    vizinhos = {}
    coords = []
    vizcoords = {}
    for x in range(r):
        for y in range(c):
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and isinstance(puzz[nx][ny], int):
                    varname = "V_{0}_{1}".format(x,y)
                    variaveis.append(varname)
                    coords.append((x,y))
    for cr in coords:
            row = cr[0]
            col = cr[1]
            vizs = []
            cvizs =[]
            varname = "V_{0}_{1}".format(row,col)
           
            if isinstance(puzz[row][col], int):
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        vizname = "V_{0}_{1}".format(r,c)
                        if r < 0 or r >= len(puzz) or c < 0 or c >= len(puzz[0]):
                            continue 
                        if r == row and c == col:
                            continue  
                        if not isinstance(puzz[r][c], int):
                            vizs.append(vizname)
                            cvizs.append((r,c))
            else:
              
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        vizname = "V_{0}_{1}".format(r,c)
                        if r < 0 or r >= len(puzz) or c < 0 or c >= len(puzz[0]):
                            continue  
                        if r == row and c == col:
                            continue  
                        if isinstance(puzz[r][c], int):
                            vizs.append(vizname)
                            cvizs.append((r,c))
            vizs=set(vizs)
            vizcoords.update({cr:cvizs})
            vizinhos.update({varname:set(vizs)})
    variaveis = sorted(set(variaveis))
    
    def minesweeper_constraint(a, A, b, B):
        return A != B

    constraints = []
    for var in vizinhos:
        for viz in vizinhos[var]:
            constraints.append((var, viz, minesweeper_constraint))
            
    dominios = {}
    for cr in coords:
        row = cr[0]
        col = cr[1]
        varname = "V_{0}_{1}".format(row,col)
        bombs = list(itertools.product([0, 1], repeat=len(coords)))
        valid_bombs = []
        for bomb_comb in bombs:
            valid = True
            for i, coord in enumerate(tuples_list):
                if bomb_comb[i] == 1 and grid[coord[0]][coord[1]] == 1:
                    valid = False
                    break
            if valid:
                valid_bombs.append(bomb_comb)
        dominios[varname] = {bomb_comb} 

    return CSP(variaveis, dominios, vizinhos,constraints)

def show_domains(dom):
    vardoms = []
    for i in dom:
        for j in i:
            vardoms.append((i,j))
    return vardoms

from copy import deepcopy 
def fill_puzzle(puzzle,sol):
    copia=deepcopy(puzzle)
    for s in sol:
        if isinstance(sol[s],int):
            xy=s.split('_')
            x=int(xy[1])
            y=int(xy[2])
            copia[y][x]='@' if sol[s] else '~'
    return copia
        
    
    