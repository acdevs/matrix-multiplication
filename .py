a=[[ 2,1],
   [ 3,2],
   [-1,1],
   [ 3,4],
   [-2,5],
   [ 4,6]]
#m x n
m=len(a); n=len(a[0])
b=[[ 1,0,1,4,6,7],
   [-1,2,1,6,5,4]]
#p x q
p=len(b); q=len(b[0])
if n==p:
    print('Calculating Product...',end='\n\n')
    x=[]
    for i in range(m):
        tmp=[]
        for j in range(q):
            sum_elem=0
            for k in range(n):
                sum_elem+= a[i][k]*b[k][j]
            tmp.append(sum_elem)
        x.append(tmp)
    for i in x:
        print('[',end='')
        for j in i:
            print(f'{str(j).rjust(3)}',end='')
        print(' ]')
else:
    print('Matrix product not possible!')
