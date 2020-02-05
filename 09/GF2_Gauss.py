# this code was taken from https://gist.github.com/popcornell/bc29d1b7ba37d824335ab7b6280f7fec
# it has been altered as follows:
# commented out import numba and @numba.jit , changed def name, imported sys.argv,
# added print statments for each step to show process, added counter for step numbers

import numpy as np
from sys import argv
# import numba

# @numba.jit(nopython=True, parallel=True) #parallel speeds up computation only over very large matrices
# M is a mxn matrix binary matrix (adjacency matrices must have adjacency defined by columns, not rows)
# all elements in M should be uint8 
def GF2_Gauss(M):

    m,n = M.shape

    i=0
    j=0
    step = 0;

    if argv[len(argv)-1] == '-Steps':
        print("Gaussian Elimination in Galois Binary Field a.k.a. GF(2): ")
        print

    while i < m and j < n: #need to add print statments for each step to show process
        # find value and index of largest element in remainder of column j
        k = np.argmax(M[i:, j]) +i

        # swap rows
        #M[[k, i]] = M[[i, k]] this doesn't work with numba
        temp = np.copy(M[k])
        M[k] = M[i]
        M[i] = temp


        aijn = M[i, j:]

        col = np.copy(M[:, j]) #make a copy otherwise M will be directly affected

        col[i] = 0 #avoid xoring pivot row with itself

        flip = np.outer(col, aijn)

        M[:, j:] = M[:, j:] ^ flip

        i += 1
        j +=1

        step += 1

        if argv[len(argv)-1] == '-Steps':
            print('Step %i :' %(step) )
            print(M)
            print

    return M

# to get a matrix to work in this, it needs to be a numpy array (use M_numpy = np.array(M))
