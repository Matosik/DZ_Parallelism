import concurrent.futures

def set_into_power_of_two(value: float)->float:
    """This function is about to set the value in power of two

    Args:
        value (float): value

    Returns:
        float: value in power of two
    """
    return (value**2.0)
    

if __name__=="__main__":
    
    str = input("Input legs(sep by space): ")
    str_args = str.split(' ')
    
    for i in range(0,2): 
        str_args[i] = float(str_args[i])
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        result = executor.map(set_into_power_of_two, str_args)
        print(sum(tuple(result))**0.5)
        
        
    
    
    
    