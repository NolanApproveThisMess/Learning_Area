import time

def typewrite(text, delay=0.05):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

typewrite("Hello! Welcome to Calculator")
try:
    first_num= int(input("Whats the first number?"))
    sec_num= int(input("Whats the second number?"))
    operators=input("Operator? type +,-,/-*")
    if operators == "+":
        rest=first_num+sec_num
        print(f"result is {rest}")
    elif operators == "-":
        rest=first_num-sec_num
        print(f"result is {rest}")
    elif operators == "/":
        rest=first_num/sec_num
        print(f"result is {rest}")
    elif operators == "*":
        rest=first_num*sec_num
        print(f"result is {rest}")
    else:
        typewrite("Invalid operator try again")
except ZeroDivisionError:
    print("Divder should not be zero")
except ValueError:
    print("Please enter valid numbers.")