#To open the file, use the built-in open() function.
def demo(file):
    with open(file,'r') as filename:
        words=filename.read()
    print(words)
    filename.close()
demo("demofile.txt")

#use of read
f=open("demofile.txt","r")
a=f.read()
print(a)
f.close()

#use of readline
x=open("demofile.txt","r")
b=x.readline()
print(b)
x.close()

# use of readlines
y=open("demofile.txt","r")
c=y.readlines()
print(c)
y.close()

# use of read numbers
p = open("demofile.txt", "r")
print(p.read(5))


#use of readline
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# use of for loop
f = open("demofile.txt", "r")
for x in f:
  print(x)


    


