import sys
import concurrent.futures
def dis(a:float,b:float,c:float)-> float:
    """Function for finding the discriminant

    Args:
        a (float): coefficient coefficient in front of x^2
        b (float): coefficient in front of x
        c (float): free coefficient

    Returns:
        float: discriminant
    """
    return b**2 - 4 *a*c
def roots(mass)->float:
    """Root Finding Roots of a Quadratic Equation 

    Args:
        mass (_type_): array with discriminant,  coefficient in front of x and  coefficient in front of x^2

    Returns:
        float: finished roots
    """
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
                arr_for_root=[]
                arr_for_root.append(diskrim)
                arr_for_root.append(arr[0])
                arr_for_root.append(arr[1])
                result=roots(arr_for_root)
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
