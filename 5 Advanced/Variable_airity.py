#Variable Arity

#Arity of a method is the number of arguments (formal parameters) it takes.
#Ideally methods have a fixed arity but Python allows methods that can have
#variable arity i.e. the methods can take variable number of arguments.
#To define a method that supports variable number of arguments the formal parameter
#is declared as : *args

def fx(*args):
	print('-----------------')
	print('datatype of args: ', type(args))
	if len(args) > 0:
		print('Values of arguments:')
		for i in args:
			print('processing : ', i)
	else:
		print('No arguments')
	print('-----------------')

#Because the formal parameter is a variable arity parameter (*args), so
#the actual parameters are packed to form a tuple that is passed as a
#parameter to fx1()
fx(1,2,3)
fx(1,2,3,4,5)
fx()
