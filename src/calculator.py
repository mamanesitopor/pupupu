from src.rpn_converter import to_rpn
from src.evaluator import evaluate_rpn

def calculate(expression: str) -> float:
    rpn = to_rpn(expression)
    return evaluate_rpn(rpn)