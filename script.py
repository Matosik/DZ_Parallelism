import sys
import concurrent.futures
def dis(a,b,c):
    return b**2 - 4 *a*c
def roots(mass):
    discr=mass[0]
    b=mass[2]
    a=mass[1]
    return (-b+discr)/(2*a)

if(__name__=="__main__"):
    arr=[]
    try:
        for i in range(1, 4):
            arr.append(float(sys.argv[i]))
        print(f"{arr[0]}x^2 + {arr[1]}x + {arr[2]} = 0\n")
        diskrim=dis(arr[0],arr[1],arr[2])
        with concurrent.futures.ProcessPoolExecutor() as ex:
            if(diskrim==0):
                result=roots(diskrim,arr[0],arr[1])
                print(result)
            elif(diskrim>0):
                x1=[diskrim**0.5, arr[0], arr[1]]
                x2=[-(diskrim**0.5), arr[0],arr[1]]
                arr_for_roots=[]
                arr_for_roots.append(x1)
                arr_for_roots.append(x2)
                result=ex.map(roots, arr_for_roots)
                print(tuple(result))
            else:
                print("Действительных корней нет !!!")
    except:
        print("Переданы не все аргументы ")
