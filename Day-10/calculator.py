from art import logo
# Calculator

# Add
def add(n1,n2):
  return n1+n2

# Subtract
def subtract(n1,n2):
  return n1-n2

# Multiply
def multiply(n1,n2):
  return n1*n2

# Divide
def divide(n1,n2):
  return n1/n2


operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  }


def calculator():
  print(logo)
  num1 = float(input("Enter a Number?: "))
  for o in operations:
    print(o)

  should_continue = True

  while should_continue:
    operations_symbol = input("Pick a symbol from above? ")
    num2 = float(input("Enter the next Number?: "))

    fun = operations[operations_symbol]
    output = fun(num1,num2)

    print(f"{num1} {operations_symbol} {num2} = {output} ")

    if input(f"Press 'y' to continue calculation with the {output} or 'n' to start with new Inputs: ") == 'y':
      num1 = output
    else:
      should_continue = False
      calculator()


calculator()

