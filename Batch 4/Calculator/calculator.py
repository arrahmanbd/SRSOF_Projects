def calculator(math):
    return eval (math)
print("="*20)
print("Calculator : X to Exit")
print('='*20)
while True:
    math=input("\n")
    if math=="x" or math=="x":
        print("Thanks for using Calculator")
        break
    else:
        print('Result:',
calculator(math))