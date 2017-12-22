#My first proper code.-------------RAJNEESH KUMAR SHARMA--------------

def add(num1, num2):
    return num1 + num2
#function for addition

def subtract(num1, num2):
    return num1 - num2
#function for subtraction

def product(num1, num2):
    return num1 * num2
#funtion for multiplication

def division(num1, num2):
    return num1/num2
#function for division

def mod(num1, num2):
    return num1 % num2
#funtion for modulus value

def power(num1, num2):
    return num1 ** num2
#function for num1 to the power num2

def mean(num1, num2):
    return (num1 + num2)/2
#function for average calculation


#Now, we are going to create the choice list(options)
print("Operations you can perform are : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus Value (Subtract Modulus Value from first number and it'll be divisible by second number)")
print("6. Exponent (Power taking first number as Base and second as Power)")
print("7. Average")

#for iteration, we have to introduce a new integer
x = 0

#to work continuously, we are going to use while loop
while True:
    #Take input choice
    choice = input("Enter your choice (1 to 7) : ")

    #take input numbers
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    #condition application
    if choice == '1':
        print(num1," + ",num2," = ",add(num1, num2))

    elif choice == '2':
        print(num1," - ",num2," = ",subtract(num1, num2))

    elif choice == '3':
        print(num1," x ",num2," = ",product(num1, num2))

    elif choice == '4':
        print(num1," / ",num2," = ",division(num1, num2))

    elif choice == '5':
        print(num1," % ",num2," = ",mod(num1, num2)," i.e. (",num1," - ",mod(num1,num2),") / ",num2," = INTEGER")

    elif choice == '6':
        print(num1,"^",num2," = ",power(num1, num2))

    elif choice == '7':
        print("Average of ",num1," and ",num2," is ",mean(num1, num2),".")

    else:
        print("INVALID INPUT")
