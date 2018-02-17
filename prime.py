PRIME = [2]
def goforit(range=100000):
	'''Use this command to search for primes.
	the range argument defines the upper limit
	default range is 100'000
	Have fun, (c) Nighmared
	----
	nighmared.github.io'''
	x = 1
	counter =0
	while x<range+1:
		x+=2
		counter +=1
		isprime = True
		TOTAL = PRIME
		for y in PRIME:
			if y*y>x:
				break
			if x%y ==0:
				isprime = False
				break
		if isprime and x !=1 and x!=0 and x not in PRIME:
			PRIME.append(x)
		if counter>(range/200):
			counter = 0
			print('{0}%'.format(round(((x/range)*100),0)))
	export(PRIME,range)
def sqrt(x):
	'''Simple Square root Function
	Will Return Square Root of x Argument'''
	return(x**0.5)
def limit(x):
	'''Used to limit the range of primes that are tested to the ones smaller than the square root of x'''
	PRIMEF = []
	sx = sqrt(x)
	for y in PRIME:
		if y>sx:
			break
		PRIMEF.append(y)
	return(PRIMEF)
def export(list,name):
	'''Writes given list into a csv file
	name argument will be the files name'''
	namestr = str(name)+'.csv'
	file = open(namestr,'w')
	for x in list:
		file.write(str(x)+'\n')
	file.close()
	print('export finished ({})'.format(name))

<<<<<<< HEAD
goforit(100000)
=======


goforit()
>>>>>>> cc43940638867f5458556be36cfa398bda5cac34
