from src.evaluator import evaluate_rpn

def test_addition():
    assert evaluate_rpn(['2', '3', '+']) == 5.0

def test_complex():
    # 1 2 3 * +  => 1 + (2*3) = 7
    assert evaluate_rpn(['1', '2', '3', '*', '+']) == 7.0