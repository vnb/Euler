#Triangular numbers
#def triangular_numbers(n): 
#    return sum(range(1,n))
# def divisors_of(n,i):
#     #divisors = 1
#     #div = 1
#     #num1 = n
#     #x = num1
#     while i<=n/2:
#         if n%i == 0:
#             i += 1
#             return divisors_of(n/i)
#         else:
            
#            divisors +=1
#            x = num1/div
#        div += 1
#    return divisors+1               
#i = 0
#a =triangular_numbers(i)
#b = divisors_of(a)
#while b<=500:
#    a =sum(range(0,i))
#    b = divisors_of(a)
#    if b>500:
#        break
#    i +=1    
#print a  
def sum_of_nat_nos(n):
	sum=n*(n+1)/2
	return(sum)
def factors(n):
	#x = 1
	factor = 2
	for i in range(2, int(n ** 0.5) + 1):
		if n%i == 0:
			#print i, n/i
			if i == n/i: factor += 1
			else: factor += 2
			#x += factors(n/i)
			#factor += 1
	# dict1[n] = factor+1
	return(factor)

print(factors(10))
"""
i = 1
ans = 1
n = 1
dict1[1] = 1
while ans<=500:
	if n in dict1
"""
i=1
while factors(sum_of_nat_nos(i))<=499:
 	i+=1
 	print(i, sum_of_nat_nos(i), factors(sum_of_nat_nos(i)))
print(sum_of_nat_nos(i), i)

