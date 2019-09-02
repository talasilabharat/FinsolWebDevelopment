f = open("myfile.txt","w")
k=input("Enter user name : ")
f.write("\n")
f.write(k)
k=input("Enter age: ")
f.write("\n")
f.write(k)
f.close()

with open("myfile.txt", "r") as f:
    for line in f:
        print(line)
f.close()
