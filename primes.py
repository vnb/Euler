import numpy
import math
#def prime(upto=100):
#    return filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))
#print sum(prime(upto=2000000))
##lambda creates a temporary function that is not bound to a name. "num" is the function here. 

natural_numbers = 1
sum1 = 1
sum2 = []
while sum1<10000000:
    natural_numbers = natural_numbers+1
    sum1 = sum1+natural_numbers
    sum2.append(sum1)




x =  filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), range(2,sum1))
l = []
for y in sum2:
    if y not in x:
      l.append(y)  
#print l      
#print type(sum2[1])

divs = 0
for i in l:
    divs = 0
    for j in range(2,1+int(math.sqrt(i))):
        if i%j == 0:
            divs = divs+1
            if divs >= 500:
                break
    print divs            
    if divs>=500:
        print i
        break
print i               
                        