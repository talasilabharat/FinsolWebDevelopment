l=[' ']
for i in range(65,123):
    if(91<=i<97):
        continue
    else:
        l.append(chr(i))
class nameError(Exception):
    def display(self):
        print("please enter a valid name.....")



while (1):
    try:
        n=input("Enter Name : ")
        if(len(n)==0):
            print("please enter a valid name.....")
            continue;
        for i in n:
            if i not in l:
                raise nameError()
            continue;
        break;
    except nameError as e:
        e.display()
while (1):
    try:
   
        x=int(input("Enter age : "))
        if (x<=0):
            print('please enter a valid age.......')
            continue;
        break;
    except ValueError:
        print('please enter a valid age.......')

        
print("\nName is ",n,"\n","Age is ",x)
