from my_or_tools import newSolver, SolVal, ObjVal

def solve_model(D,Start=None, End=None):
    s,n = newSolver('Shortest path problem'),len(D)
    if Start is None: 
        Start,End = 0,len(D)-1
    G = [[s.NumVar(0,1 if D[i][j] else 0,'') \
        for j in range(n)] for i in range(n)]
    for i in range(n): 
        if i == Start:
            s.Add(1 == sum(G[Start][j] for j in range(n))) 
            s.Add(0 == sum(G[j][Start] for j in range(n))) 
        elif i == End:
            s.Add(1 == sum(G[j][End] for j in range(n))) 
            s.Add(0 == sum(G[End][j] for j in range(n))) 
        else:
            s.Add(sum(G[i][j] for j in range(n)) ==
                sum(G[j][i] for j in range(n))) 
        s.Minimize(s.Sum(G[i][j]*(0 if D[i][j] is None else D[i][j]) \
                for i in range(n) for j in range(n))) 
    rc = s.Solve()
    Path,Cost,Cumul,node=[Start],[0],[0],Start
    while rc == 0 and node != End and len(Path)<n:
        next = [i for i in range(n) if SolVal(G[node][i]) == 1][0]
        Path.append(next)
        Cost.append(D[node][next])
        Cumul.append(Cumul[-1]+Cost[-1])
        node = next
    return rc,ObjVal(s),Path,Cost,Cumul