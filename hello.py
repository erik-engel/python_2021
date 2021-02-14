import sys

def main(name):

    if name == 'Alice' or name == 'Jens':
        print("Hello " + name)
    else:
        print('You are not a real person')

        
main(sys.argv[1])