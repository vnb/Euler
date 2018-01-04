import numpy as np
A = np.arange(1,2000001).reshape(200000,10)
P = A[0][2]
row = 0
j = 1
prime = []
sum_primes = 2
new_numb = 0
for a in range(0,200000):
    for b in range(0,10):
        if (b+1)%2 == 0 or (b+1)%5 == 0:
            A[a][b] = 0
A[0][1] =2
A[0][4] = 5         
while P<=2000000:
    print P
    new_numb = 0
    #print sum_primes
    sum_primes = sum_primes+P
    #print len(prime)
    prime.append(P)
    for l in range(row,199999):
        for m in range(0,9):
            if A[l][m]%P == 0 and A[l][m] <>1 and A[l][m]<>P:
                A[l][m] = 0
            if new_numb == 0 and A[l][m]>P:
                P1 = A[l][m]
                new_numb = 1
                row = l
    P = P1                                         
print sum_primes   