import numpy as np
A = np.arange(2,20)
prime = [2]
print A
b = []
p = 2
while p<=20:
    for i in A:
        if i%p <> 0:  
            b.append(i)
    for l in b:
        if l>p:
            m = l
            break
    p = m          
    print p
    b = []
    prime.append(p)
    b=prime
    print "----"              
print A 
print prime       