import re

def tokenize(expression: str) -> list:
    """
    Разбивает строку выражения на токены (числа, операторы, скобки).
    """
    # Регулярка ищет числа (включая дробные) или символы операторов
    token_pattern = r'\d+(?:\.\d+)?|[+\-*/^()]'
    tokens = re.findall(token_pattern, expression)
    return tokens