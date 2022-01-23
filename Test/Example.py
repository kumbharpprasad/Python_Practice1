import math

#Math examples

'''
#Area of Circle
pi= math.pi
r= 3**2
print(r)
circle= pi*r
print (f"Circle Area = {circle}")

#Find all prim numbers

start=11
end=20

for i in range(start, end+1):
    if i>1:
        for j in range(2, i):
            if (i % j==0):
                break
        else:
            print(i)
'''


