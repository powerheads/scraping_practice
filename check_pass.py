def check_password():
    attempts = 3
    while attempts > 0:
        password = input("Enter password: ")

        if password == "1234":
            return True
        else:
            attempts -= 1
            print("Wrong password.Try again.")
            print("Attempts left:", attempts)
    
        

def ask_continue():
   while True:
    ans = input("continue? (yes/no) :")
    if ans == "yes":
        return True
    elif ans == "no":
         return False
    else: print("Invalid answer")
   

def doing_business(ass):
    if ass:
        print("Doing Business")
        input("press any key...")
    


while True:
    ok=check_password()
    if not ok:
        print("Access Denied")
    else:
        print("Access Granted")
    doing_business(ok)
    if not ask_continue():
        print("Bye, press any key...")
        input()
        break  