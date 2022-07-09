
import re
from fractions import Fraction

print(''' Hello.!! I can solve any frcations. please enter your expressions separates by space for logical operators.
eg: 2_3/8 + 9/8 (mixed fractions must be given with "_")''')
print("\nEnter your expression:")

# define variables as required
x = str(input())
space = " "
operands = "*+-"
list = []

# check the input expressions if logical operators are separated
def check_input(x):
    for i in x:
        for item in operands:
            if i == item:
                check_before = (x.index(i) - 1)
                check_after = (x.index(i) + 1)
            # print(check_space)
                for before in x[check_before]:
                    for after in x[check_after]:
                        if before.isspace() != True:
                            print("Error: input should be separated with space between logical operators. eg: '2_3/8 + 9/8'")
                        elif after.isspace() != True:
                            print("Error: input should be separated with space between logical operators. eg: '2_3/8 + 9/8'")
                        else:
                            global error
                            error = str(x)
        return

check_input(x)
'''
Function to calculate only fractions & mixed fractions from the input expression.
# output the decimal result to list, leaving the logical operators. eg:['0.57', '*', '33.25', '-', '2.06'].
'''
def solve_fraction(x):
    # first remove unwanted charecters from input
    x = re.sub('[!@#$%^&()={};:,<>`~?]', '', x)
    x = x + " " * len(x)
    # split the input with space b/w logical operator
    if space in x:
        x = x.split(space)
        for i in x:
            if "_" in i:
                i = i.split("_")
                for i in i:
                    if "/" in i:
                        i = i.split("/")
                        numerator = float(i[0])
                        denominator = float(i[1])
                    else:
                        mixednum = int(i)
                new_numerator = (mixednum * denominator) + numerator
                i = str(new_numerator / denominator)
            elif "/" in i:
                i = i.split("/")
                d_numerator = float(i[0])
                d_denominator = float(i[1])
                i = str(d_numerator / d_denominator)

            list.append(i)
            global result
            result = list

#Function to calculate the result with logical operators.
def calculate(x):
    solve_fraction(x)
    seq = ""
    for item in result:
        seq += (item)
    global decimal
    decimal = eval(seq)
    print('Decimal result: {}'.format(decimal))

# Function to get decimal value and convert to Fractional result
def for_fractional(x):
  calculate(x)
  x = Fraction(decimal)
  fractional_result = x.limit_denominator()
  print('Fractional result: {}'.format(fractional_result))

for_fractional(x)


