# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
shop_list =  OrderedDict()
for _ in range(n):
    items = input().rsplit(maxsplit=1)
    
    if shop_list.setdefault(items[0], 0):
        shop_list[items[0]] += int(items[-1])
    else:
        shop_list[items[0]] = int(items[-1])

for key, value  in shop_list.items():
    print(key, value)
    