"""Unit tests for template-driven question generators in math_tutor_drills."""
import pytest
from math_tutor_drills.templatedriven_question_genera import (
    LinearEquationGenerator,
    FactoringGenerator,
    TriangleProblemGenerator,
)

class TestLinearEquationGenerator:
    def test_generate_returns_latex_and_answer(self):
        gen = LinearEquationGenerator()
        question, answer = gen.generate()
        assert question.startswith("Solve: $")
        assert answer.startswith("$x = ")

    def test_generate_varies_output(self):
        gen = LinearEquationGenerator()
        results = set(gen.generate() for _ in range(10))
        assert len(results) > 1

class TestFactoringGenerator:
    def test_generate_returns_latex_and_answer(self):
        gen = FactoringGenerator()
        question, answer = gen.generate()
        assert question.startswith("Factor: $")
        assert answer.startswith("$(x")

    def test_generate_varies_output(self):
        gen = FactoringGenerator()
        results = set(gen.generate() for _ in range(10))
        assert len(results) > 1

class TestTriangleProblemGenerator:
    def test_generate_returns_latex_and_answer(self):
        gen = TriangleProblemGenerator()
        question, answer = gen.generate()
        assert "right triangle" in question
        assert answer.startswith("$c = ")

    def test_generate_varies_output(self):
        gen = TriangleProblemGenerator()
        results = set(gen.generate() for _ in range(10))
        assert len(results) > 1

# Edge cases
@pytest.mark.parametrize("min_coef,max_coef", [(1, 1), (5, 5)])
def test_linear_equation_fixed_coef(min_coef, max_coef):
    gen = LinearEquationGenerator(min_coef=min_coef, max_coef=max_coef)
    question, answer = gen.generate()
    assert question.startswith("Solve: $")
    assert answer.startswith("$x = ")

@pytest.mark.parametrize("min_root,max_root", [(-1, -1), (2, 2)])
def test_factoring_fixed_root(min_root, max_root):
    gen = FactoringGenerator(min_root=min_root, max_root=max_root)
    question, answer = gen.generate()
    assert question.startswith("Factor: $")
    assert answer.startswith("$(x")

@pytest.mark.parametrize("min_leg,max_leg", [(3, 3), (7, 7)])
def test_triangle_fixed_leg(min_leg, max_leg):
    gen = TriangleProblemGenerator(min_leg=min_leg, max_leg=max_leg)
    question, answer = gen.generate()
    assert "right triangle" in question
    assert answer.startswith("$c = ")
