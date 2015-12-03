# single-source shortest paths
# algorithm:Dijkstra


def Dijkstra(m, n, v):
    '''
    m:matrix<-dis
    n:the number of nodes
    v:source node
    '''
    global D
    D = [m[0][i] for i in range(n)]
    D[v] = 0
    set1 = set({})
    set2 = set([i for i in range(n)])
    set1.add(v)
    set2.remove(v)
    print(D)
    # loop:

    while len(set1) != n:
        mini = min([D[i] for i in set2])
        for i in set2:
            if D[i] == mini:
                flag = i
                break
        set1.add(flag)
        set2.remove(flag)
        D[flag] = mini
        for i in set2:
            #print("D[i]=%d" % D[i])
            #print("D[flag]=%d" % D[flag])
            #print("m[flag][i]=%d" % m[flag][i])
            D[i] = min(D[i], D[flag] + m[flag][i])
    print(D)

# test:
inf = 65536
edges = []  # the input file
V = {}  # V.keys():nodes
D = []  # the initial array
for i in open("in.txt", 'r'):
    edges.append(i.split(" "))
for i in range(len(edges)):
    V[edges[i][0]] = 1
    V[edges[i][1]] = 1
n = len(V)  # n:the number of nodes
dis = [[inf] * n for i in range(n)]
for i in edges:
    i = [int(x) for x in i]
    dis[i[0]][i[1]] = i[2]

#***
Dijkstra(dis, n, 0)
