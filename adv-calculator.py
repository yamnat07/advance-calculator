def take_choice():
    while True:
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                return 1
            elif choice==2:
                return 2
            else:
                print("Enter a valid choice.")   
        except ValueError:
            print("Enter a valid value!!")
          

def take_num1():
    while True:
        try:
            num1=float(input("Enter first number: "))
            return num1
        except ValueError:
            print("Enter a valid value!!")


def take_num2():
    while True:
        try:
            num2=float(input("Enter second number: "))
            return num2
        except ValueError:
            print("Enter a valid value!!")


def take_op():
    while True:
        print("Select operation: ")
        print("For addition: +,Result=num1+num2")
        print("For subtraction: -,Result=num1-num2")
        print("For multiplication: *,Result=num1*num2")
        print("For division: /,num1/num2")
        print("For remainder after division: %,Result=num1%num2")
        print("For power: **,Result=num1**num2\n")
        op=input("Enter the operator: ")
        if op in["+","-","*","/","**","%"]:
            return op
        else:
            print("Enter a valid operator!!")


def calculate():
    taken_num1=take_num1()
    taken_num2=take_num2()
    taken_op=take_op()
    while True:
        try: 
         if taken_op=="+":
            print(f"The sum is: {taken_num1+taken_num2}")
            break
         elif taken_op=="-":
            print(f"The difference is: {taken_num1-taken_num2}")
            break
         elif taken_op=="*":
            print(f"The product is: {taken_num1*taken_num2}")
            break
         elif taken_op=="/":
            print(f"The answer is: {taken_num1/taken_num2}")
            break
         elif taken_op=="%":
            print(f"The remainder is: {taken_num1%taken_num2}")
            break
         elif taken_op=="**":
            print(f"The answer is: {taken_num1**taken_num2}")
            break
        except ZeroDivisionError:
            print("Division by zero is not defined!!")
            taken_num1=take_num1()
            taken_num2=take_num2()
            taken_op=take_op()
            



def main(): 
    while True:
        print("####################################")
        print("~~~~~~~~~ADVANCE CALCULATOR~~~~~~~~~")
        print("####################################\n")
        print("1.Do a calculation.")
        print("2.Exit.")
        chosen=take_choice()
        if chosen==1:
            calculate()
            print("The program is ready for next operation.")
        elif chosen==2:
            print("Thank you!")
            break
main()                        

