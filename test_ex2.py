
from ex2 import solve_model, solve_model1
def main():
    import sys
    import tableutils
    m=3
    n=7
    if len(sys.argv)<=1:
        print('Usage is main [data|run]')
        return
    C=[[23, 0, 19, 25, 14, 0, 22, 551],
       [16, 0, 0, 20, 23, 13, 23, 689],
       [22, 28, 11, 0, 20, 13, 24, 634],
       [288, 234, 236, 231, 247, 262, 281, 0]]
    A=[[125, 234, 150, 120, 150, 150, 110],
       [150, 234, 200, 190, 130, 140, 150],
       [75, 234, 100, 160, 110, 130, 90]]
    X = 60
    if sys.argv[1]=='data':
        for i in range(m):
            C[i].insert(0,'Plant '+str(i))
        C[-1].insert(0,'Demand')
        C.insert(0,['From/To']+['City '+str(i) for i in range(n)]+['Supply'])
        tableutils.printmat(C)
    elif sys.argv[1]=='run0':
        rc,Value,G=solve_model(C,A)
        T=[]
        for i in range(m):
            T.append([0 for j in range(n+1)])
            tot = 0
            for j in range(n):
                T[i][j] = int(G[i][j])
                tot += int(G[i][j])
            T[i][-1] = tot
        TT = []
        for j in range(n):
            TT.append(sum([T[i][j] for i in range(m)]))
        TT.insert(0,'Total')
        T.append(TT)
        for i in range(m):
            T[i].insert(0,'Plant '+str(i))

        T.insert(0,['From/To']+['City '+str(i) for i in range(n)]+['Total'])
        
        print(rc, Value)
        tableutils.printmat(T)
        tableutils.printmat(G)

    elif sys.argv[1]=='run1':
        rc,Value,G=solve_model1(C,X)
        T=[]
        for i in range(m):
            T.append([0 for j in range(n+1)])
            tot = 0
            for j in range(n):
                T[i][j] = int(G[i][j])
                tot += int(G[i][j])
            T[i][-1] = tot
        TT = []
        for j in range(n):
            TT.append(sum([T[i][j] for i in range(m)]))
        TT.insert(0,'Total')
        T.append(TT)
        for i in range(m):
            T[i].insert(0,'Plant '+str(i))

        T.insert(0,['From/To']+['City '+str(i) for i in range(n)]+['Total'])
        
        print(rc, Value)
        tableutils.printmat(T)
        tableutils.printmat(G)

main()
