
from ex1 import solve_model
def main():
    import sys
    import tableutils
    n=5
    header=[]
    if len(sys.argv)<=1:
        print('Usage is main [data|run0|run1]')
        return
    
    C = [[0,4,4,0,0],
         [4,0,0,2,0],
         [4,0,0,2,3],
         [0,2,2,0,6],
         [0,0,3,6,0]]
    S = [0]
    T = [4]
    
    for i in range(n):
        h='N'+str(i)
        if i in S:
            h=h+'-S'
        elif i in T:
            h=h+'-T'
        header.append(h)
    if sys.argv[1]=='data':
        tableutils.printmat(tableutils.wrapmat(C,header,header))
    elif sys.argv[1][0:3]=='run':
        rc,Fout,Fin,x=solve_model(C,S,T,sys.argv[1][3:4]=='1')
        tableutils.printmat(tableutils.wrapmat(x,header,[str(int(Fout))+'-'+str(int(Fin))]+header))
        print(rc, Fout, Fin, x)


main()
