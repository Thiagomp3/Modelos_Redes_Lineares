from Caminho_rapido_b import solve_model
def main():
    import sys
    import tableutils
    n=10
    header = ['P'+str(i) for i in range(n)]
    if len(sys.argv)<=1:
        print('Usage is main [data|run]')
        return
    C=[[0,0,12,0,0,0,0,0,0,0],
       [20,0,0,18,0,0,0,0,0,0],
       [0,0,0,32,18,0,0,0,0,0],
       [0,18,32,0,0,28,0,0,25,0],
       [0,0,0,0,0,30,13,0,0,0],
       [0,0,0,28,30,0,0,0,21,49],
       [0,0,0,0,0,0,0,0,0,38],
       [0,18,0,0,0,0,0,0,36,0],
       [0,0,0,25,0,21,0,36,0,40],
       [0,0,0,0,0,49,0,28,40,0]]




    if sys.argv[1]=='data':
        for i in range(n):
            C[i].insert(0,'P'+str(i))
        C.insert(0,['']+header)
        tableutils.printmat(C)
    elif sys.argv[1]=='run':
        rc,Value,Path,Cost,Cumul=solve_model(C)
        Path.insert(0,'Points')
        Cost.insert(0,'Distance')
        Cumul.insert(0,'Cumulative')
        T=[Path,Cost,Cumul]
        tableutils.printmat(T,True)
main()