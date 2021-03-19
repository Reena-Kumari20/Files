with open("people1_exercise.txt","r") as my_file:
    head=[next(my_file) for x in range(4)]
print(head)