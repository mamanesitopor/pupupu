def evaluate_rpn(rpn_tokens: list) -> float:
    """
    Вычисляет результат выражения в обратной польской нотации.
    """
    stack = []

    for token in rpn_tokens:
        if token.replace('.', '').lstrip('-').isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0: raise ZeroDivisionError("Division by zero")
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]