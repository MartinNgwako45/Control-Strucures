num1 = int(input("please enter a number "))


sumNum = num1
i = 1
while True:
    n = int(input("input a number"))
    if n == -1:
        break

    sumNum += n
    i += 1

average = sumNum / i
print (f'The average number is {average}')
