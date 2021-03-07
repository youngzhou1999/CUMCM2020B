import networkx as nx
import numpy as np

# ´Ë´úÂëÀûÓÃfloydËã·¨Çó½â³ö×î¶Ì¾àÀë¾ØÕóD

def func1(node,edge):
    g = nx.Graph()
    g.add_nodes_from(node)
    g.add_edges_from(edge)
    nx.draw(g,with_labels = True)
    A = np.array(nx.adjacency_matrix(g).todense())
    d = nx.floyd_warshall_numpy(g)
    return A,d


edge1 = [(1,2),(1,25),
        (2,3),
        (3,4),(3,25),
        (4,5),(4,25),(4,24),
        (5,6),(5,24),
        (6,7),(6,23),(6,24),
        (7,8),(7,22),
        (8,9),(8,22),
        (9,10),(9,15),(9,16),(9,17),(9,21),
        (10,11),(10,13),(10,15),
        (11,12),(11,13),
        (12,13),(12,14),
        (13,14),(13,15),
        (14,15),(14,16),
        (15,16),
        (16,17),(16,18),
        (17,18),(17,21),
        (18,19),(18,20),
        (19,20),
        (20,21),
        (21,22),(21,23),(21,27),
        (22,23),
        (23,24),(23,26),
        (24,25),(24,26),
        (25,26),
        (26,27)
       ]
node1 = np.array(range(1,27))

a1,d1 = func1(node1,edge1)

def legal(i,j,id):
    if(id>64 or id<1):
        return False
    if(j==1):
        if(id>=(i-1)*8+2 and id<=i*8):
            return True
        else:
            return False
    if(j==2):
        if(i%2==0):
            if(id>=8*i+1 and id<=8*i+1+6):
                return True
            else:
                return False
        else:
            if(id>=8*i+1 and id<=8*i+1+6):
                return True
            else:
                return False
    if(j==3):
        if(i%2==0):
            if(id>=8*i+2 and id<=8*i+2+6):
                return True
            else:
                return False
        else:
            if(id>=8*i+1 and id<=8*i+7):
                return True
            else:
                return False

def bound(x):
    if(x>=1 and x<=8):
        return 1
    if(x>=9 and x<=16):
        return 2
    if(x>=17 and x<=24):
        return 3
    if(x>=25 and x<=32):
        return 4
    if(x>=33 and x<=40):
        return 5
    if(x>=41 and x<=48):
        return 6
    if(x>=49 and x<=56):
        return 7
    if(x>=57 and x<=64):
        return 8

edge2 = []
for i in range(1,65):
    x = bound(i)
    if(x%2!=0):
        if(legal(x,1,i+1)):
            edge2.append((i,i+1))
        if(legal(x,2,i+7)):
            edge2.append((i,i+7))
        if(legal(x,3,i+8)):
            edge2.append((i,i+8))
    else:
        if(legal(x,1,i+1)):
            edge2.append((i,i+1))
        if(legal(x,2,i+8)):
            edge2.append((i,i+8))
        if(legal(x,3,i+9)):
            edge2.append((i,i+9))

node2 = np.array(range(1,65))

a2,d2 = func1(node2,edge2)