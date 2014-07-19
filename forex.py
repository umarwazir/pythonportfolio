def forexcalc(r, c):
    return float(r) * float(c)
r = raw_input("Currency rate:")
c = raw_input("Amount: ")
f = forexcalc(r, c)
print "Conversion: ", f