import sys

def greeting(x):
	#print(x)

	if len(x) == 2 and x[1] == '-it':
		print('interactive terminal started')
	if len(x) == 3 and x[2] == '--rm':
		print('Will be removed at exit')

greeting(sys.argv)
