"""Core module for math_tutor_drills."""

from __future__ import annotations
import random
from typing import Any, Dict, List, Optional, Tuple

from .types import MathTutorDrillsOptions, MathTutorDrillsResult
from .exceptions import ValidationError
from ._utils import validate_not_empty

class LinearEquationGenerator:
    """Generates linear equation questions and answers.

    Example::
        gen = LinearEquationGenerator()
        q, a = gen.generate()
    """
    def __init__(self, min_coef: int = 1, max_coef: int = 10, min_const: int = 0, max_const: int = 20) -> None:
        self.min_coef = min_coef
        self.max_coef = max_coef
        self.min_const = min_const
        self.max_const = max_const

    def generate(self) -> Tuple[str, str]:
        """Generate a random linear equation and its solution.

        Returns:
            Tuple of (question_latex, answer_latex)
        """
        a = random.randint(self.min_coef, self.max_coef)
        b = random.randint(self.min_const, self.max_const)
        x = random.randint(-10, 10)
        c = a * x + b
        question = f"Solve: ${a}x + {b} = {c}$"
        answer = f"$x = {x}$"
        return question, answer

class FactoringGenerator:
    """Generates factoring quadratic questions and answers.

    Example::
        gen = FactoringGenerator()
        q, a = gen.generate()
    """
    def __init__(self, min_root: int = -10, max_root: int = 10) -> None:
        self.min_root = min_root
        self.max_root = max_root

    def generate(self) -> Tuple[str, str]:
        """Generate a random quadratic to factor and its solution.

        Returns:
            Tuple of (question_latex, answer_latex)
        """
        r1 = random.randint(self.min_root, self.max_root)
        r2 = random.randint(self.min_root, self.max_root)
        while r1 == r2:
            r2 = random.randint(self.min_root, self.max_root)
        a = 1
        b = -(r1 + r2)
        c = r1 * r2
        question = f"Factor: $x^2 + {b:+}x + {c:+}$"
        answer = f"$(x {r1:+})(x {r2:+})$"
        return question, answer

class TriangleProblemGenerator:
    """Generates triangle geometry questions and answers (Pythagorean theorem).

    Example::
        gen = TriangleProblemGenerator()
        q, a = gen.generate()
    """
    def __init__(self, min_leg: int = 3, max_leg: int = 20) -> None:
        self.min_leg = min_leg
        self.max_leg = max_leg

    def generate(self) -> Tuple[str, str]:
        """Generate a right triangle problem and its solution.

        Returns:
            Tuple of (question_latex, answer_latex)
        """
        a = random.randint(self.min_leg, self.max_leg)
        b = random.randint(self.min_leg, self.max_leg)
        c = (a ** 2 + b ** 2) ** 0.5
        question = f"Given a right triangle with legs $a={a}$ and $b={b}$, find the hypotenuse $c$."
        answer = f"$c = \\sqrt{{{a}^2 + {b}^2}} = {c:.2f}$"
        return question, answer

class MathTutorDrills:
    """Generate and grade algebra/geometry drill sets with LaTeX and answer keys.

    Example::

        from math_tutor_drills import MathTutorDrills

        instance = MathTutorDrills()
        result = instance.run()
        print(result)
    """

    def __init__(self, options: MathTutorDrillsOptions | None = None) -> None:
        self.options = options or MathTutorDrillsOptions()

    def run(self) -> MathTutorDrillsResult:
        """Execute the main operation.

        Returns:
            MathTutorDrillsResult with the operation outcome.
        """
        try:
            feature_1 = self.options.feature_1 or {}
            num_questions = feature_1.get("num_questions", 5)
            types = feature_1.get("types", ["linear", "factoring", "triangle"])
            questions: List[Dict[str, Any]] = []
            for _ in range(num_questions):
                qtype = random.choice(types)
                if qtype == "linear":
                    q, a = LinearEquationGenerator().generate()
                elif qtype == "factoring":
                    q, a = FactoringGenerator().generate()
                elif qtype == "triangle":
                    q, a = TriangleProblemGenerator().generate()
                else:
                    raise ValidationError(f"Unknown question type: {qtype}")
                questions.append({"type": qtype, "question": q, "answer": a})
            return MathTutorDrillsResult(success=True, data={"questions": questions})
        except Exception as e:
            return MathTutorDrillsResult(success=False, error=str(e))
