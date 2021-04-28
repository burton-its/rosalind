#k = homozygous dominant AA
#m = heterozygous Aa
#n = homozygous recessive aa


#P(Aa/AA) = k*(k-1)+(k*m+m*k)+(k*n+n*k)+0.75m(m-1)+(0.5m*n+0.5n*m)/ t*(t-1)

#what is the chance given k,m,n parents. that you will have a dominant allele

#punnet squares give us  
#.1k*m, 1k*n, 1k*(k-1)
#.1m*k, .5m*n, .75m*(m-1)
#.1n*k, .5n*m, 0n*(n-1)

#so we use .5*n*m + .5*n*m = m*n, .25*m(m-1), n*(n-1), then subtract from 1 for probablity of dominant allele

k = 2
m = 2
n = 2
t = k + m + n

tot = (1 - (((m*n) + (.25*m*(m-1)) + (n*(n-1)) )/ (t*(t-1))))

print(tot)
# (m*n + .25*m*(m-1) + n*(n-1)/ (n*(n-1))


