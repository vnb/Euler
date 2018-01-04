#Prime Numbers
prime = range(2,200000)
fact = range(2,200000)
j = 0
sum1 = 2
print sum1
while j<len(prime)-1:
    sum1 = sum1+prime[j]
    for k in fact:
        mult = prime[j]*k
        if k>=prime[j]:
            if mult in prime:
                del prime[prime.index(mult)] 
        if mult>=prime[-1]: 
            break              
    j += 1
    fact = [l for l in prime if l>prime[j]]
print prime   