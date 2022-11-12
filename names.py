# reading the name from the keyboard
names = str(input("enter names of pupils in a class"))
print(names)

# initialising the variable count_names to 1
count_names = 1


while True: # creating while loop and setting the condition to true
    pupil_names= input("john ")

    if pupil_names == "stop":
        print(f"there are {count_names} students")
        break                                    # breaking out of the loop

    count_names += 1


while True:# creating while loop and setting the condition to true 
    pupil_names = input("loli ")
    print("there are {count_names} students")
    break

# allocating total numner of students 
print(f"there are {names_count} students")

 
