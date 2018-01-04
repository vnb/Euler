#Find the largest prime factor of 600851475143
def prime_list_generator(n):
#    #Lets try the sieve
#    print "--"
#    prime_numbers = range(2,n)
#    print "--"
#    i = 0
#
#    while i<n**0.5:
#        num = prime_numbers[i]
#        t = len(prime_numbers)-1
#        s = []
#        for j in range(0,t):
#            if prime_numbers[j]%num==0 and prime_numbers[j]<>num:
#                indx = prime_numbers.index(prime_numbers[j])
#                s.append(indx)            
#        new_primes = []
#        for k in s:
#            new_primes.append(prime_numbers[k])
#        #print new_primes
#        l3 = [x for x in prime_numbers if x not in new_primes]
#        prime_numbers = l3
#        i += 1             
#    return prime_numbers
#print prime_list_generator(600851475143)       
    i = 1
    k = 0
    st1 = []
    st2 = []
    while i<n/2:
        if i<>n and n%i==0 and i<>1:
            st1.append(i)
            st2.append(n/i)
            st3 = st1+st2
        for ele in st1:
            if ele in st2:
                k = 1
                break;
        if k == 1:
            break;            
        st = str(i+2)
        st = list(st)
        sum_num = 0
        for x in st:
            sum_num = int(x)+sum_num
        if sum_num%3<>0 or int(st[-1]) <>5 or int(st[-1])<>0:        
            i+=2        
    fin = st3[0]
    fin1 = 0
    st4 = []
    while fin <max(st3):
        for k in st3:
            if k<>fin and k%fin==0:
                st4.append(k)
        fin1 = fin1+1
        fin = st3[fin1]    
    return max([x for x in st3 if x not in st4])        
print prime_list_generator(600851475143)     
#def prime_factors(n):
#    b = []
#    if n%2 == 0:
#        a = range(2,n/2,2)
#    else:
#        a = range(2,round(n/2),2)
#    for i in a:
#        if sum(list(str(a)))%3 == 0 or list(str(a))[-1] == '5' or list(str(a))[-1] == '0':
#            b.append(a)
#    c = ([j for j in a if j not in b])                
#    return c                 
#print prime_factors(600)               
##600851475143






































