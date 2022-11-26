import numpy as np

def extract(eps):
    '''Entrée : matrice 3x3 de la déformation
       Sortie : matrice 2x2 [ [eps1,1 ; eps1,3] ; [eps1,3 ; eps3,3] '''
    return np.array([[eps[0,0], eps[0,2]], [eps[0,2], eps[2,2]]])

# Testé et approuvé

def diagonalize(eps):
    tab, t = np.linalg.eig(eps)
    return np.array([[tab[0], 0], [0, tab[1]]])

# Testé et approuvé