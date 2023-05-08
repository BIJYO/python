a=int(input("enter number A :"))
b=int(input("enter number B :"))


print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch=int(input("Enter Choice : "))

if ch==1:
   
    c=a+b
    print("Sum = ",c)
elif ch==2:
   
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    
    c=a*b
    print("Product = ",c)
elif ch==4:
   
    c=a/b
    print("Division = ",c)
else:
    print("Invalid Choice")
