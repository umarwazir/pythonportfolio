largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")         #Asking for input
    if num == "done" : break
    if len(num) < 1 : break
    try:
        num = int(num)
    except:
        print "Invalid input"
        continue
    if largest is None:
        largest = num   
    if num > largest:
        largest = num
    if smallest is None:
        smallest = num
    if num < smallest:
        smallest = num
print "Maximum is ", largest
print "Minimum is ", smallest