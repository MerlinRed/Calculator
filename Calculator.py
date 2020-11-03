import re

operands = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,
}

print("Enter '+' to add up the two numbers\n"
      "Enter '-' to subtract two numbers\n"
      "Enter '*' to multiply two numbers\n"
      "Enter '/' to divide two numbers\n"
      "Enter '**' to exponentiating number\n"
      "Enter '//' for integer division\n"
      "Enter '%' to get the remainder of the division\n"
      "Enter 'exit' to exit")


def calculator():
    while True:
        print('-' * 20)
        try:
            user_input = input('Enter example: ')
            num_1 = re.search(r'[\d]+', user_input)
            operand = re.search(r'[\+\-\*\/\%]+', user_input)
            num_2 = re.search(r'[\d]+$', user_input)
            if user_input == 'exit':
                exit()
            if operand.group() in operands:
                func = operands[operand.group()]
                result = func(int(num_1.group()), int(num_2.group()))
                print(f'The answer is: {result}')
            print('-' * 20)
        except ValueError:
            continue
        except AttributeError:
            continue


calculator()
