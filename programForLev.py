import math

a = [0,2,5,1,2,5,8,2]

for i in range(8):
    for j in range(7):
        if (a[i] > a[j]):
            c = a[i]
            a[i] = a[j]
            a[j] = c
          
print(a)

#LevPrivet =)
    
