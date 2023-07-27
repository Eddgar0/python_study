from sys import argv
# linecounter
counter = 0 
f = open(argv[1])
for t in f:
    line = t.strip()
    if  line and not line.startswith('#'):
        counter += 1
f.close()
print(counter)