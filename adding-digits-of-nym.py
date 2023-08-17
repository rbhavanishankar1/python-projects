#adding of digits of the number
num=input("enter the two digit number :")
print(num)
sum=0
for i in range(0,len(num)):
    sum=sum+int(num[i])
print("sum of the given digits is : ",sum)

#print(int(num[0])+int(num[1]))