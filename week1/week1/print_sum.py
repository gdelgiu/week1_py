from sys import argv

argc = len(argv)

#checks

if argc > 3:
    print('too many args')
    exit()
elif argc < 3:
    print('too little args')
    exit()

try:
    values = int(argv[1]), int(argv[2])
except:
    print('not an int')
    exit()

print(values[0] + values[1])



