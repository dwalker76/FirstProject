import math

a = [0,2,5,1,2,5,8,2]

for i in range(len(a)):
    for j in range(len(a) - 1):
        if (a[i] > a[j]):
            #c = a[i]
            #a[i] = a[j]
            #a[j] = c
            a[i],a[j] = a[j],a[i]
            
print(a)
for i in range(len(a)):
    print(a[i])
    
#LevPrivet =)

#Privet
