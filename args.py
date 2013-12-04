def func(*args):
	print "Number of arguments:", len(args)
	sum = 0
	for value in args:
			sum += value
	print "Sum of the arguments:", sum

if __name__ == "__main__":
		func(12)
		func(5, 8, 2)
		func(18, -2, 50, 21, 6)

