import random


def generate_boolean_value(p_true, p_false):
    if p_true + p_false == 100:
        return random.choice([True] * p_true + [False] * p_false)
    else:
        return random.choice([True] * 50 + [False] * 50)