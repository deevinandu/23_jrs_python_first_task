num = int(input("enter a no."))
d=0
while num!=0:
    d+=1
    num = int(num/10)

print("no of digits = ", d)