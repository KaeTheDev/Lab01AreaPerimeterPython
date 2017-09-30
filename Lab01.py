print("Welcome to KaeTheDev's PYTHON Room Detail Generator!")

#Prints Blank Line
print()

#Allows user to input how many calculations they'd like to perform
value = int(input("How many calculations would you like to perform? "))

print()

while value > 0:
    value -= 1
    print()
    
    #Asks the user for the length
    length = int(input("Enter length: "))


    #Asks the user for the width
    width = int(input("Enter width: "))

    #Calculates the area
    area = length * width

    #Calculates the perimeter
    perimeter = (length * 2) + (width * 2)

    print()
    
    #Prints the area
    print('Area: ', area)


    #Prints the perimeter
    print('Perimeter: ', perimeter)
    

