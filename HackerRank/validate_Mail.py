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
import re


def fun(s):
    # return True if s is a valid email, else return False
    pattern = re.compile(r'[A-Za-z0-9\-\_]+@[A-Za-z0-9\.]+\.[A-Za-z]{1,3}$')
    if pattern.match(s):
        return True
    else:
        return False
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input('Insterte cantidad de Mails'))
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)