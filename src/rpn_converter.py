from src.tokenizer import tokenize

OPERATORS = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
    '^': 3
}

def to_rpn(expression: str) -> list:
    """
    Преобразует инфиксную запись в постфиксную (ОПН).
    """
    tokens = tokenize(expression)
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.replace('.', '').isdigit():
            output_queue.append(token)
        elif token in OPERATORS:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   OPERATORS.get(operator_stack[-1], 0) >= OPERATORS[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop() # Удаляем '('

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue