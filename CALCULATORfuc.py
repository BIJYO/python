print("CALCULATOR\n\n\n")
print("1.addition\n")
print("2.subtraction\n")
print("3.multiplication\n")
print("4.divition\n")
ch=int(input("Enter Choice : "))
    if ch==1:
   
        su=n1+n2
        print("Sum = ",su)
    elif ch==2:
n1=float(input("Enter a number : "))
n2=float(input("Enter a number : "))
def su(n1,n2):
    
   
        su=n1-n2
        print("Difference = ",su)
    elif  ch==3:
    
        su=n1*n2
        print("Product = ",su)
    elif ch==4:
   
        su=n1/n2
        print("Division = ",su)
    else:
        print("Invalid Choice")
        su=n1+n2
 
    return(su)
x=su(n1,n2)
    
print(x)



