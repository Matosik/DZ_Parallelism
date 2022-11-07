import concurrent.futures

def squared(b:float)-> float:
    return b**2.0

def two_part(a:float,c:float)->float:
    return 4*a*c
def root_squared(dis:float)->float:
    return dis**0.5

def root_denominator(a:float)->float:
    return a*2
def root_numerator(dis:float, b:float)->float:
    if(dis>0):
        return (-b+dis, -b-dis)
    elif(dis==0):
        return -b

if(__name__=="__main__"):
    a,b,c=map(float, input("Input a,b,c(with space): ").split())
    with concurrent.futures.ProcessPoolExecutor() as ex:

        diskrim=0
        diskrim+=squared(b)
        diskrim-=two_part(a,c)
        diskrim=root_squared(diskrim)

        if(diskrim==0):
            root=root_numerator(diskrim,b)
            root/=root_denominator(a)
            print(root)
        elif(diskrim<0):
            print("Действительных корней нет")
        else:
            root_1,root_2=root_numerator(diskrim,b)
            root_1/=root_denominator(a)
            root_2/=root_denominator(a)
            print(root_1,root_2)


