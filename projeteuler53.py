import math
a=0
def komb(x,y):
    return math.factorial(x)/math.factorial(y)/math.factorial(x-y)
for i in range(23,101):
    for b in range(1,i):
       if komb(i,b)>1000000:
           a+=1
print(a)