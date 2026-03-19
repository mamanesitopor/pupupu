from src.tokenizer import tokenize

def test_simple_numbers():
    assert tokenize("12 + 5") == ['12', '+', '5']

def test_floats():
    assert tokenize("1.5 + 2.5") == ['1.5', '+', '2.5']

def test_parentheses():
    assert tokenize("(1+2)") == ['(', '1', '+', '2', ')']