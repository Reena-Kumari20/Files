f=open("people1_exercise.txt","r")
a=f.read()
print(a)
f.close()
def a():
    f=open("people1_exercise.txt","r")
    count=0
    for i in f:
        if i!="\n":
            count=count+1
    f.close()
    print("this is navgurukul first batch's students",count)
a()

"""f=open("people1_exercise.txt","r")
count=0
for i in f:
    if i!="\n":
        count=count+1
f.close()
print(count)"""