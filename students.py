m1=int(input ("enter the enter the marks of the sudent 1:  "))
m2=int(input ("enter the enter the marks of the sudent 2:  "))
m3=int(input ("enter the enter the marks of the sudent 3:  "))
m4=int(input ("enter the enter the marks of the sudent 4:  "))
m5=int(input ("enter the enter the marks of the sudent 5:  "))
m6=int(input ("enter the enter the marks of the sudent 6:  "))
l2= [m1,m2,m3,m4,m5,m6]
l2.sort()
print(l2)
# to find the sum of the list 
print(l2[0] + l2[1] + l2[3] + l2[4] + l2[5])

print(sum(l2))