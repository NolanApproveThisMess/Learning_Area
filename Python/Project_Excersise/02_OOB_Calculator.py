# Will gotta use OOB class and mehtod to create calculator

import time

def typer(text, delay= 0.05):
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
        if operator == "+":
            result= self.first + self.second
            return f"Result: {result}"
        elif operator == "-":
            result= self.first - self.second
            return f"Result: {result}"
        elif operator == "/":
            result= self.first / self.second
            return f"Result: {result}"
        elif operator == "*":
            result= self.first * self.second
            return f"Result: {result}"
        else:
            return "Invalid Please Try again"
while True:
    typer("Welcome to mini Calculator!")
    typer("Please put your first number")
    first=input()
    if isinstance(first,int):
        first = float(first)
    typer("Please put your second number")
    second=input()


        