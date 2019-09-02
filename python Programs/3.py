def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

n1=int(input("Enter Operand1 : "))
op=input("Enter Basic Operation")
n2=int(input("Enter operand2 : "))

if  op== "+":
    k=add(n1,n2)
    print(n1,"+",n2,"=",k)


elif  op=="-":
    l=sub(n1,n2)
    print(n1,"-",n2,"=",l)

  
elif  op=="*":
    m=mul(n1,n2)
    print(n1,"*",n2,"=",m)

  
elif  op=="/":
    n=div(n1,n2)
    print(n1,"/",n2,"=",n)

  
elif  op=="%":
    o=mod(n1,n2)
    print(n1,"%",n2,"=",o)

else:
    print("Please enter basic operation")


  
