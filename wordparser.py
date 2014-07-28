fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "Invalid file name!"
    exit()
dict = list()
for lines in fh:
    lines = lines.split()
    for words in lines: 
        if words in dict: continue
        dict.append(words)
dict.sort()
print dict