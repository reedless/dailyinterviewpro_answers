'''
Given a mathematical expression with just single digits, plus signs, negative signs,
and brackets, evaluate the expression. Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
'''

def evalHelper(exp):
    if (len(exp) == 0):
        print("wthhhhhhhhhhhh")
        return
    c = exp[0]
    rest = exp[1:]
    print(exp)
    print(c)
    if (len(exp) == 1):
        return int(c)
    if (c == '+'):
        return evalHelper(rest)
    elif (c == '-'):
        return -(evalHelper(rest))
    elif (c == '('):
        count = 0
        i = 0
        for char in exp:
            if (char == '('):
                count += 1
            if (char == ')'):
                count -= 1
            if (count == 0):
                break
            i += 1
            print(i)
        print(exp[1:i])
        return evalHelper(exp[1:i]) + evalHelper(exp[i+2:])
    else:
        print('else')
        return int(c) + evalHelper(rest)


def eval(expression):
    expression = expression.replace(" ", "")
    return evalHelper(expression)

print (eval('- ( 3 + ( 2 - 1 ) )'))
# -4
