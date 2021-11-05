from my_or_tools import ObjVal, SolVal, newSolver

def solve_model(C,S,T,unique=True):
    s,n = newSolver('Maximum flow problem'),len(C)
    x=[[s.NumVar(0,C[i][j],'')for j in range(n)]for i in range(n)]  
    B=sum(C[i][j] for i in range(n) for j in range(n))
    Flowout,Flowin  = s.NumVar(0,B,''),s.NumVar(0,B,'')
    for i in range(n):
        if i not in S and i not in T:
            s.Add(sum(x[i][j] for j in range(n)) == \
            sum(x[j][i] for j in range(n))) 
    s.Add(Flowout == s.Sum(x[i][j] for i in S for j in range(n)))
    s.Add(Flowin  == s.Sum(x[j][i] for i in S for j in range(n)))
    s.Maximize(Flowout-2*Flowin if unique else Flowout-Flowin) 
    rc = s.Solve()
    return rc,SolVal(Flowout),SolVal(Flowin),SolVal(x)