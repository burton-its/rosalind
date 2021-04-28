in1 = open("rosalind_gc.txt","r")

d1 = {}
tempgc = 0.0
templab = ""


for line in in1:
	if line.startswith(">"):
		nuc = line.strip("\n").strip(">")
		d1[nuc] = ""
	else:
		d1[nuc] += line.strip("\n")

maxgc = 0.0
maxlab = ""

	
#gc content
for i in d1:
	seq = d1[i]
	c = seq.count("C")
	g = seq.count("G")
	templen = len(seq)
	tempgc = (c+g)/templen * 100
	print(i,tempgc)
	if tempgc > maxgc:
		maxgc = tempgc
		maxlab = i


print('MAX ',maxlab,maxgc)
