# Resta
def resta(n1,n2):
    """ Resta dos numeros """
    try:
        a,b = int(n1),int(n2)
    except ValueError as e:
        print('los valores deben ser numeros')
        raise e
    
    return a - b