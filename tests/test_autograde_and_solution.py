"""Unit tests for auto-grading and worked_solution methods in math_tutor_drills."""
import pytest
from math_tutor_drills.templatedriven_question_genera import (
    LinearEquationGenerator,
    FactoringGenerator,
    TriangleProblemGenerator,
)
from math_tutor_drills.exceptions import ValidationError

def test_linear_equation_autograde_and_solution():
    gen = LinearEquationGenerator()
    q, a = gen.generate()
    # Extract x value from answer
    x_val = int(a.replace('$x =', '').replace('$', '').strip())
    # Correct answer
    result = gen.grade(str(x_val))
    assert result['correct'] is True
    # Incorrect answer
    result = gen.grade(str(x_val + 1))
    assert result['correct'] is False
    # Worked solution contains all steps
    sol = gen.worked_solution()
    assert 'Given:' in sol and 'Final answer' in sol
    # Error if called before generate
    gen2 = LinearEquationGenerator()
    with pytest.raises(ValidationError):
        gen2.grade('5')
    with pytest.raises(ValidationError):
        gen2.worked_solution()

def test_factoring_autograde_and_solution():
    gen = FactoringGenerator()
    q, a = gen.generate()
    # Extract roots from answer
    import re
    m = re.findall(r'\(x ([+-]) (\d+)\)', a)
    assert m and len(m) == 2
    r1 = int(m[0][1] + m[0][2])
    r2 = int(m[1][1] + m[1][2])
    # Accept either order
    ans1 = f'(x {"+" if r1 >= 0 else "-"} {abs(r1)})(x {"+" if r2 >= 0 else "-"} {abs(r2)})'
    ans2 = f'(x {"+" if r2 >= 0 else "-"} {abs(r2)})(x {"+" if r1 >= 0 else "-"} {abs(r1)})'
    assert gen.grade(ans1)['correct'] is True
    assert gen.grade(ans2)['correct'] is True
    # Incorrect
    assert gen.grade('(x + 99)(x - 99)')['correct'] is False
    # Worked solution contains all steps
    sol = gen.worked_solution()
    assert 'Given:' in sol and 'Final answer' in sol
    # Error if called before generate
    gen2 = FactoringGenerator()
    with pytest.raises(ValidationError):
        gen2.grade('(x + 1)(x - 1)')
    with pytest.raises(ValidationError):
        gen2.worked_solution()

def test_triangle_autograde_and_solution():
    gen = TriangleProblemGenerator()
    q, a = gen.generate()
    # Extract c value from answer
    import re
    m = re.search(r'= ([\d.]+)\$', a)
    assert m
    c_val = float(m.group(1))
    # Accept close float
    assert gen.grade(f'{c_val:.2f}')['correct'] is True
    # Accept small error
    assert gen.grade(f'{c_val + 0.009:.2f}')['correct'] is True
    # Incorrect
    assert gen.grade(f'{c_val + 0.1:.2f}')['correct'] is False
    # Worked solution contains all steps
    sol = gen.worked_solution()
    assert 'Given:' in sol and 'Final answer' in sol
    # Error if called before generate
    gen2 = TriangleProblemGenerator()
    with pytest.raises(ValidationError):
        gen2.grade('5.00')
    with pytest.raises(ValidationError):
        gen2.worked_solution()
