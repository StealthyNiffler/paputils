import sympy
import re

def texify_expr(expr, *args):
    """expr should be a string with a valid python math expression and subs should
    be a list containing tuples with the name and the value of every variable that
    you want to substitute
    example: texify_expr(x/(sqrt(y + z)), ("x", 3), ("y", 1))"""
    latex_expr = sympy.latex(sympy.sympify(expr), mul_symbol="dot")
    if args:
        for sub in args:
            latex_expr = re.sub(sub[0], str(sub[1]), latex_expr)
    print(latex_expr)

def new_round(num, precision):
    if precision == 0:
        return int(num)
    return round(num, precision)

def texify_table(precision, cols, *args):
    """takes iterables as input and return latex table as string
        example: texify_table(precision, cols, *args)"""
    if cols != 1:
        n = max([len(elem) for elem in args])
        rows = n//cols
        arguments = []
        for i in range(cols):
            for elem in args:
                arguments.append(list(elem[rows*i:rows*(i+1)]))
        return texify_table(precision, 1, *arguments)
    table = ""
    for i in range(0, len(args[0])):
        for j, col in enumerate(args):
            if i < len(col):
                table += str(new_round(float(col[i]), precision))
            else:
                table += " "
            if j != len(args)-1:
                table += " & "
            else:
                table += " \\\\"
        table += "\n"
    return table

def get_stats(vals, precision=3):
    """ return median and standard derrivative:
    syntax: get_stats(vals, precision=3)
    """
    n = len(vals)
    avr = new_round(np.sum(vals)/n, precision)
    sig = new_round(np.sqrt(1/(n-1) * np.sum((vals - avr)**2)), precision)
    der = new_round(np.sqrt(1/(n*(n-1)) * np.sum((vals - avr)**2)), precision)
    return avr, sig, der
