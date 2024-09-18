import random
def unit_vector(x,y,z):
    mag=(x*x+y*y+z*z)**0.5
    print(f'({x}/{mag:.2f},{y}/{mag:.2f},{z}/{mag:.2f})')

def scalar_multiple(n,x,y,z):
    x_n=x*n
    y_n=y*n
    z_n=z*n
    print(f'({x_n},{y_n},{z_n})')

def equality_test(x,y,z,i,j,k):
    if x==i and y==j and z==k:
        print('Vectors are equal')
    else:
        print('Vectors are not equal')

def cross_product(x,y,z,i,j,k):
    det_i=y*k-j*z
    det_j=-(x*k-i*z)
    det_k=x*j-y*i
    print(f'{det_i},{det_j},{det_k}')
def main():
    # 1st vector t
    tx=random.randint(5,10)
    ty=random.randint(5,10)
    tz=random.randint(5,10)
    print(f' tx: {tx} , ty: {ty} , tz: {tz}')
    # 2nd vector m
    mx=random.randint(5,10)
    my=random.randint(5,10)
    mz=random.randint(5,10)
    print(f' mx: {mx} , my: {my} , mz: {mz}')
    # 3rd vector b
    bx=random.randint(5,10)
    by=random.randint(5,10)
    bz=random.randint(5,10)
    print(f' bx: {bx} , by: {by} , tz: {bz}')
    # Task2
    print('Unit Vector is: ',end='')
    unit_vector(mx,my,mz)
    #Task3
    n=int(input('Enter the multiple n: '))
    print('Scalar Multiple: ',end='')
    scalar_multiple(n,bx,by,bz)
    #Task4
    print('Cross Product:',end='' )
    cross_product(tx,ty,tz,bx,by,bz)
    #task5
    print('Equality Test: ' ,end='' )
    equality_test(mx,my,mz,tx,ty,tz)
main()