def is_median(x,y,z):
	# Returns True if x is the median of the group x,y,z
	if x <= y and x >= z or x>=y and x<=z:
		return True
	else:
		return False

def get_median_of_three(a,b,c):
	if is_median(a,b,c):
		return a
	if is_median(b,c,a):
		return b
	else:
		return c

def run_test():
	print("The median of [0,0,0] is %d" % get_median_of_three(0,0,0))
	print("The median of [10,2,6] is %d" % get_median_of_three(10,2,6))
	print("The median of [100,-100,-100] is %d" % get_median_of_three(100,-100,-100))
	print("The median of [1,1,9] is %d" % get_median_of_three(1,1,9))

if __name__ == "__main__":
    run_test()	
