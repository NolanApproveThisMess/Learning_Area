# Will gotta use OOB class and mehtod to create calculator

import time

def typer(text, delay= 0.005):
    for i in text:
        print(i, end="", flush= True)
        time.sleep(delay)
    print()

class Calculator:
    def __init__(self, first, second, operator):
        self.first=first
        self.second=second
        self.operator= operator

    def calculate(self):
        while True:
            try:
                if self.operator == "+":
                    return self.first + self.second
                elif self.operator == "-":
                    return self.first - self.second
                elif self.operator == "/":
                    return self.first / self.second
                elif self.operator == "*":
                    return self.first * self.second
                else:
                    return "Invalid Please Try again"
            except ZeroDivisionError:
                return ("Second number for division should not be 0. Please try again")


        
def calculus():
    while True:
        try:
            typer("Welcome! Please iput the first number!")
            fist=int(input())
            break
        except ValueError:
            typer("Opps thats not a number, please try again!")
    while True:
        try:
            typer("What's the second number?")
            secs=int(input())

            break
        except ValueError:
            typer("Opps thats not a number, please try again!")

    while True:
        typer("What's the operator? type any of these: +,-,*,/")
        ops=input()
        if ops in ("+","-","/","*"):
            break
        else:
            typer("Not on the list. Try again")
    
    return fist,secs,ops

magic=calculus()
calc=Calculator(*magic)
typer(f"Result: {calc.calculate()}")        


def exits():
    while True:
        try:
            typer("Wanna try again? type Y if yes, N if no")
            ans=input().upper()
            if ans == ("Y"):
                magics=calculus()
                calc=Calculator(*magics)
                typer(f"Result: {calc.calculate()}")
            elif ans ==("N"):
                typer("Got it! Bye!")
                break
            else:
                typer("nope, try again. It's Y or N")
        except ValueError:
            typer("Try again folks")

exits()




        