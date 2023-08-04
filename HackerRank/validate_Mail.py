# You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
# 
# 
# Valid email addresses must follow these rules:
# 
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores .
# The website name can only have letters and digits .
# The extension can only contain letters .
# The maximum length of the extension is .



def fun(s):
    # return True if s is a valid email, else return False
    splitted_mail = s.plit('@')

    if len(splitted_mail) != 2:
        return False
    
    #if 


# verifico @ y parto por arroba si no hay exactamente 2, bobo error
# Colocar el username aparte y analizarlo
# colocar el dominio aparte y dividirlo de derecha a izquierda por punto 
# Si tiene mas de 2 bobo error
# validar 2 nivel de dominio
# analizar el 1 nivel de dominio
# si todos son verdaderos arroja verdadero


    pass
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)