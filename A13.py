##1.Write a Python program to read  lines of a file.

f = open("aaa.txt","w")
f.write("Don't try to search me you can't .")

f = open("aaa.txt","r")
print(f.read())


##2.Write a Python program to copy the contents of a file to another file

a = open("aaa.txt","r")
content = a.read()
b = open("bbb.txt","w")
b.write(content)
b = open("bbb.txt","r")
print("\n\n",b.read())


##3.Write a Python program to combine each line from first file with the corresponding line in second file.

print()
with open("aaa.txt","r") as x:
    with open("bbb.txt","r") as y:
        for line1,line2 in zip(x.readlines(),y.readlines()):
            print(line1,line2)

x.close()
y.close()
        
		
