def computepay(h, r):
	if h <= 40:
		return float(h) * float(r)
	elif h > 40:
		return (40 * float(r)) + ((float(h) - 40) * (float(r) * 1.5))
h = raw_input("Enter hours: ")
r = raw_input("Enter rate: ")
p = computepay(h, r)
print "Pay due is (GBP): ", p 
