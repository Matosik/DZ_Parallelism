import concurrent.futures
def dis(a,b,c):
    return b**2 - 4 *a*c
def roots(mass):
    discr=mass[0]
    b=mass[2]
    a=mass[1]
    return (-b+discr)/(2*a)

if(__name__=="__main__"):
    a,b,c=map(float, input("Input a,b,c(with space): ").split())
    print(f"{a}x^2 + {b}x + {c} = 0\n")
    diskrim=dis(a,b,c)
    with concurrent.futures.ProcessPoolExecutor() as ex:
        if(diskrim==0):
            result=roots(diskrim,a,b)
            print(result)
        elif(diskrim>0):
            x1=[diskrim**0.5, a, b]
            x2=[-(diskrim**0.5), a,b]
            c=[]
            c.append(x1)
            c.append(x2)
            result=ex.map(roots, c)
            i=0
            print(tuple(result))
        else:
            print("Действительных корней нет !!!")
