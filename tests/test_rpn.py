from src.rpn_converter import to_rpn

def test_no_precedence():
    # 1 + 2 + 3 -> 1 2 + 3 +
    assert to_rpn("1 + 2 + 3") == ['1', '2', '+', '3', '+']

def test_precedence_mul_add():
    # 1 + 2 * 3 -> 1 2 3 * +
    assert to_rpn("1 + 2 * 3") == ['1', '2', '3', '*', '+']

def test_precedence_power():
    # 2 ^ 3 * 2 -> 2 3 ^ 2 * (Power has higher priority than mul)
    assert to_rpn("2 ^ 3 * 2") == ['2', '3', '^', '2', '*']

def test_parentheses_override():
    # (1 + 2) * 3 -> 1 2 + 3 *
    assert to_rpn("(1 + 2) * 3") == ['1', '2', '+', '3', '*']