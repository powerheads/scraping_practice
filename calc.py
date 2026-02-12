
while True:
    print("Input First Number")
    a = float(input())

    print("Input Second Number")
    b = float(input())

    print("Select action: +, -, *, /")
    action = input()

    if action == "+":
        print(a + b)
    elif action == "-":
        print(a - b)
    elif action == "*":
        print(a * b)
    elif action == "/":
        if b == 0:
            print("division by zero")
        else:
            print(a / b)
    else:
        print("Unknown action")

    print("Want calc more? (yes/no)")
    calc = input()
    if calc == "yes" : print("Here we go"); continue   
    if calc == "no": print("Task ended"); print("Press any key to exit..."); input()
    break
    