
def calculate_result(operator, op1, op2):
  o1 = int(op1)
  o2 = int(op2)
  if (operator == '+'):
    return o1 + o2
  elif (operator == '-'):
    return o1 - o2


def arithmetic_arranger(problems, res=False):
    arranged_problems = ""
    first_line = []
    second_line = []
    third_line = []
    res_line = []

    if (len(problems) > 5):
        return 'Error: Too many problems.'
    else:
        for i in range(len(problems)):
            if (problems[i].find('*') != -1 or problems[i].find('/') != -1):
                return "Error: Operator must be '+' or '-'."
            operands = problems[i].split()
        
            if not (operands[0].isdigit() and operands[2].isdigit()):
                return 'Error: Numbers must only contain digits.'
            if (len(operands[0]) > 4 or len(operands[2]) > 4):
                return 'Error: Numbers cannot be more than four digits.'
            
            max_len_per_prom = max(len(operands[0]), len(operands[2])) + 2
            space_between_prom = 4

            first_line.append((max_len_per_prom - len(operands[0])) * ' ' + operands[0])
            second_line.append(operands[1] + (max_len_per_prom - 1 - len(operands[2])) * ' ' + operands[2])
            third_line.append(max_len_per_prom * '-')
            result = str(calculate_result(operands[1], operands[0], operands[2]))
            res_line.append((max_len_per_prom - len(result)) * ' ' + result)

    for line in first_line:
        arranged_problems = arranged_problems + line
        if (line != first_line[-1]):
            arranged_problems =  arranged_problems + 4 * ' '                
    arranged_problems = arranged_problems + '\n'
    
    for line in second_line:
        arranged_problems = arranged_problems + line
        if (line != second_line[-1]):
            arranged_problems =  arranged_problems + 4 * ' '
    
    arranged_problems = arranged_problems + '\n'    
    for i in range(len(third_line)):
        arranged_problems = arranged_problems + third_line[i]
        if (i != len(third_line) - 1):
            arranged_problems =  arranged_problems + 4 * ' '
    
    if (res==True):
        arranged_problems = arranged_problems + '\n'
        for line in res_line:
            arranged_problems = arranged_problems + line
            if (line != res_line[-1]):
                arranged_problems =  arranged_problems + 4 * ' '
    return arranged_problems

# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))

expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]).rstrip()

print(actual == expected)