import sys




def goforit(range=100000,output=True):
	PRIME = [2]
	'''Use this command to search for primes.
	the range argument defines the upper limit
	default range is 100'000
	Have fun, (c) Nighmared
	----
	nighmared.github.io'''
	x = 1
	counter =0
	while x<range:
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
		if isprime and x !=1 and x!=0 and x<=range:
			PRIME.append(x)
		if counter>(range/200):
			counter = 0
			perc = round(((x/range)*100),0)
			if perc>100:
				perc = 100
			if output:
				print('{0}%'.format(perc))
	export(PRIME,range,output)


def export(list,name,output=True):
	'''Writes given list into a csv file
	name argument will be the files name'''
	namestr = str(name)+'.csv'
	file = open(namestr,'w')
	for x in list:
		file.write(str(x)+'\n')
	file.close()
	if output:
		print('export finished ({})'.format(name))
	else:
		return('export finished ({})'.format(name))

try: goforit(int(sys.argv[1]))
except IndexError:
	None