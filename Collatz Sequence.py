
collatz_dict={}
x = 0
add = 1
for i in range(1,1000000):
    x = i
    collatz_dict[i] = 1
    while x >1:
        if x%2 == 0:
            x = x/2
            if x not in collatz_dict:
                collatz_dict[i] += 1
            else:
                collatz_dict[i] = collatz_dict[i]+collatz_dict[x]
                break
        else:
            x = 3*x+1
            if x not in collatz_dict:
                collatz_dict[i] += 1
            else:
                collatz_dict[i] = collatz_dict[i]+collatz_dict[x]
                break
print(max(collatz_dict, key=collatz_dict.get))
