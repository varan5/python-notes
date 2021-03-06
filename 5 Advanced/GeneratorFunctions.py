#Generator Functions

#Generator functions use "yield" statement to
#transfer a value and the program control
#back to the caller with the state of the function
#retained in the Stack Segment.

#On next call the function resumes execution
#from the point it yielded last.

#As a generator function ends normally or due
#to return then its state is lost (deallocated)
#and next call will be a new beginning.


#        a b c(a+b)
#      a b c(a+b)
#0 1 1 2 3 5 8 13 21 34 55 89 ...
def fibonacciSeries(MAX=100):
	a = -1
	b = 1
	while True:
		c = a+b #0 1 1 2 3 5 8 ...
		if c > MAX:
			break
		yield c
		a = b #1 0 1 1 2 3 ...
		b = c #0 1 1 2 3 5 ..

def main():
	#iterate over the list
	for x in fibonacciSeries(200):
		print(x, end=' ')

main()