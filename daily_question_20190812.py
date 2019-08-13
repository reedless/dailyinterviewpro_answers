'''
Given a mathematical expression with just single digits, plus signs, negative signs,
and brackets, evaluate the expression. Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
'''

def evalHelper(exp):
    if (len(exp) == 0):
        return 0
    if (len(exp) == 1):
        return int(exp)

    c = exp[0]
    if (c == '+'):
        return eval(exp[1:])
    if (c == '-'):
        return -(eval(exp[1:]))
    if (c == '('):
        count = 0
        for i in range(len(exp)):
            if (exp[i] == '('):
                count += 1
            if (exp[i] == ')'):
                count -= 1
            if (count == 0):
                return eval(exp[1:i]) + eval(exp[i+1:])
        print("Invalid expression, missing closing parenthesis")
        return 0
    return int(c) + eval(exp[1:])


def eval(expression):
    expression = expression.replace(" ", "")
    return evalHelper(expression)

print (eval('- ( 3 + ( 2 - 1 ) )'))
# -4
print (eval('3 + ( 5 - 2 ) - ( 7 - 4 )'))
# 3
