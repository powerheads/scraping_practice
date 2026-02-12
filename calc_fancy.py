def read_float(prompt):
    while True:
        v=input(prompt)
        try:
            return float(v)
        except ValueError:
            print("not a number, try again...")
def calculate(a, b, operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b==0: 
            print("division by ZERO")
            return None
        return a/b
def read_operation(prompt):
    while True:
        op = input(prompt)
        if op in ["+", "-", "*", "/"]:
            return op
        print("invalid operation, try again...")

def print_result(result):
    print(result)
def continius():
    while True:
        cont = input("Want calc more? (yes/no): ")
        if cont == "yes":
            print("Here we go")
            return True
        elif cont == "no":
            print("Task ended")
            print("Press any key to exit...")
            input()
            return False
        else:
            print("invalid answer, try again...")
while True:   
   a=read_float("input A: ")
   operation=read_operation("input operation (+, -, *, /): ")
   b=read_float("input B: ")
   result = calculate(a,b,operation)
   print_result(result)
   if not continius():
       break