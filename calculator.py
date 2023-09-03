#Calculator
from art import logo

import os
#Addition
def add(n1, n2):
  return n1 + n2
  
#Substraction
def sub(n1, n2):
  return n1 - n2
  
#Multiplication
def mul(n1, n2):
  return n1 * n2
  
#Divison
def div(n1, n2):
  return n1 / n2

operations = {"+": add, "-": sub, "*": mul, "/": div}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?"))
  for operand in operations:
    print(operand)
  operation_symbol = input("Pick an operation")
  num2 = float(input("What's the Second number?"))
  operation_function = operations[operation_symbol]
  output = operation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {output}")
  ask = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calculation")
  
  while ask == "y":
    num1 = output
    for operand in operations:
      print(operand)
    operation_symbol = input("Pick an operation")
    num4 = float(input("What's the next number?"))
    operation_function = operations[operation_symbol]
    output = operation_function(output, num4)
    print(f"{num1} {operation_symbol} {num4} = {output}")
    ask = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calulcation.")
    
  if ask == "n":
    os.system('clear')
    calculator()
    


calculator()