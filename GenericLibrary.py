##Generic Functions Library
#####
##0.0.0. "Hello World"
print "Hello World"
#####
#####
##0.0.1 "computepay"
##Description: Small function for calculating pay using a variable rate
def computepay(h, r):														#Defining function name and inputs
    if h <= 40:																#Conditionality for lower rate
        return float(h) * float(r)											#
    elif h > 40:															#Conditionality for higher rate
        return (40 * float(r)) + ((float(h) - 40) * (float(r) * 1.5))		#
#####
#####
##0.0.2 "Countdown"
print "Initiating Countdown..."
n = 10
while n > 0:
    print n
    n = n - 1
    continue
print "Countdown Complete"
print n
######