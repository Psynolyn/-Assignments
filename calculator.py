calculating = True
while(calculating):
    num_a = float(input("Input first number: "))
    num_b = float(input("Input second number: "))
    operator = input("Input operator: ")

    match(operator):
        case "+":
            print(f'{num_a} + {num_b} = {num_a+num_b}')
        case "-":
            print(f'{num_a} - {num_b} = {num_a-num_b}')
        case ("*"):
            print(f'{num_a} * {num_b} = {num_a*num_b}')
        case "/":
            if (num_b == 0):
                print(f'{num_a} / {num_b} = Undefined')
            else:
                print(f'{num_a} / {num_b} = {num_a/num_b}')
        case _:
            print("Invalid operator, please enter +, -, * or /")

    repeat = input("Continue? y/n : ")
    calculating = False if repeat == "n" else True 


