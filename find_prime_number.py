#finding the prime number
n=int(input("enter the number to check wheather given number iws prime number or not :"))
def prime():
    pcount=0
    for i in range(2,n+1):
        n1=n%i
        if n1==0 :
            pcount+=1
    if pcount>1:
        print(f"The number : {n} is not prime number")
    else:
        print(f"The number : {n} is  prime number")    
prime()
    