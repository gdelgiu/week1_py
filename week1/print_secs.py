from sys import argv

argc = len(argv)

if argc > 4:
    print('too many args')
    exit(0)
elif argc < 4:
    print('too little args')
    exit(0)

try:
    print(int(argv[1]) * (60 ** 2) + int(argv[2]) * 60 + int(argv[3]))
except:
    print('wrong values')