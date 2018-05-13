import sys
list = open("genlist.txt").read().split(',')
def isprime(n):
	if str(n) in open('{}.csv'.format(chooselist(n))).read().split('\n'):
		return '{} is a prime'.format(n)
	else:
		return '{} isnt a prime'.format(n)
def chooselist(n):
	for x in list:
		if n<=int(x):
			return x
			break

if len(sys.argv)>1:
	print(isprime(int(sys.argv[1])))