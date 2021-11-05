from my_or_tools import ObjVal, SolVal, newSolver

def solve_model(D,E):
    s = newSolver('Mincost flow problem')
    m,n = len(D)-1,len(D[0])-1
    B = sum([D[-1][j] for j in range(n)])
    G = [[s.NumVar(0,B if D[i][j] else 0,'') for j in range(n)] \
        for i in range(m)]  
    for i in range(m): 
        for j in range(n):
            s.Add(D[i][-1] >= sum(G[i][j] for j in range(n))) 
            s.Add(D[-1][j] == sum(G[i][j] for i in range(m)))
            s.Add(G[i][j] <= E[i][j])
    Cost=s.Sum(G[i][j]*D[i][j] for i in range(m)for j in range(n)) 
    s.Minimize(Cost)
    rc = s.Solve()
    return rc,ObjVal(s),SolVal(G)

def solve_model1(D,F):
    s = newSolver('Mincost flow problem')
    m,n = len(D)-1,len(D[0])-1
    B = sum([D[-1][j] for j in range(n)])
    G = [[s.NumVar(0,B if D[i][j] else 0,'') for j in range(n)] \
        for i in range(m)]  
    for i in range(m): 
        for j in range(n):
            s.Add(D[i][-1] >= sum(G[i][j] for j in range(n))) 
            s.Add(D[-1][j] == sum(G[i][j] for i in range(m)))
            if j != 1:
                s.Add((G[i][j]/D[-1][j])*100 <= F)
    Cost=s.Sum(G[i][j]*D[i][j] for i in range(m)for j in range(n)) 
    s.Minimize(Cost)
    rc = s.Solve()
    return rc,ObjVal(s),SolVal(G)