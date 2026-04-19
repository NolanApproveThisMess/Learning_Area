# Hey just a practice. No UI or whatever. Just a  simple calculator that can do basic operations.

import time

def timer(sec, delay=0.01):
    for i in sec:
        print(i,end="", flush=True)
        time.sleep(delay)
    print()

def calculate():
    while True:
        try:
            timer ("What's the first number?")
            first_num=int(input())
            break
        except ValueError:
            timer("Not an integer! Try again")

    while True:
        try:
            timer ("What's the second number?")
            sec_num=int(input())
            break
        except ValueError:
            timer("Not an integer! Try again")

    while True:
        timer ("what's the operator")
        operator=input()
        if operator in ("+","-","/","*"):
            break
        else:
            timer("Not on the list. Try again")        

    while True:
        try:
            if operator == "+":
                result=first_num + sec_num
                timer("The result is")
                print(f":{result}")
                break
            elif operator == "-":
                result=first_num - sec_num
                timer("The result is")
                print(f":{result}")
                break
            elif operator == "*":
                result=first_num * sec_num
                timer("The result is")
                print(f":{result}")
                break
            elif operator == "/":
                result=first_num / sec_num
                timer("The result is")
                print(f":{result}")
                break
        except ZeroDivisionError:
            timer("Divisor cannot be 0, try again")
            break

def exitse():
    while True:
        try:
            timer("Wanna go and try again? type \"Y\" if yes and \"N\"if no")
            answer = input().upper()
            if answer == ("Y"):
                calculate()
            elif answer == ("N"):
                timer("Got it! Bye!")
                break
            else:
                timer("nope, try again. It's Y or N")
        except ValueError:
            timer("Try again folks")

calculate()
exitse()



