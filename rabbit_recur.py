n = 5
k = 3

#fn = number of rabbits in nth generation, rn is immature rabbits and Rn is mature rabbits
# math for this is Fn = Rn = rn
#rn = k * Rn-1
#Rn = Rn-1 + rn-1
#Fn = Rn-1 + rn-1 + k * Rn-1
#...
#Fn = Fn-1 + K * Fn-2 - important formula


# start with 1 pair alive per generation
fn1 = 1
fn2 = 1


for i in range(2,n):
	fn1,fn2 = fn2, fn1 * k + fn2
print(fn2)

	



