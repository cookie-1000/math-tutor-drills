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
        grade_result = gen.grade(user_answer="5")
        solution = gen.worked_solution()
    """
    def __init__(self, min_coef: int = 1, max_coef: int = 10, min_const: int = 0, max_const: int = 20) -> None:
        self.min_coef = min_coef
        self.max_coef = max_coef
        self.min_const = min_const
        self.max_const = max_const
        self._last_a: Optional[int] = None
        self._last_b: Optional[int] = None
        self._last_x: Optional[int] = None
        self._last_c: Optional[int] = None

    def generate(self) -> Tuple[str, str]:
        """Generate a random linear equation and its solution.

        Returns:
            Tuple of (question_latex, answer_latex)
        """
        a = random.randint(self.min_coef, self.max_coef)
        b = random.randint(self.min_const, self.max_const)
        x = random.randint(-10, 10)
        c = a * x + b
        self._last_a = a
        self._last_b = b
        self._last_x = x
        self._last_c = c
        question = f"Solve: ${a}x + {b} = {c}$"
        answer = f"$x = {x}$"
        return question, answer

    def grade(self, user_answer: str) -> Dict[str, Any]:
        """Grade a user's answer for the last generated question.

        Args:
            user_answer: The user's answer as a string (e.g., '5').
        Returns:
            Dict with keys: correct (bool), expected (str), user (str), explanation (str)
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if self._last_x is None:
            raise ValidationError("No question generated yet.")
        try:
            user_val = int(user_answer.strip().replace('$x =', '').replace('x =', '').replace('$', '').strip())
        except Exception:
            return {"correct": False, "expected": str(self._last_x), "user": user_answer, "explanation": "Could not parse answer as integer."}
        correct = (user_val == self._last_x)
        return {
            "correct": correct,
            "expected": str(self._last_x),
            "user": str(user_val),
            "explanation": "Correct!" if correct else f"Expected x = {self._last_x}"
        }

    def worked_solution(self) -> str:
        """Return a step-by-step solution for the last generated question.

        Returns:
            Step-by-step solution as a string.
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if None in (self._last_a, self._last_b, self._last_c, self._last_x):
            raise ValidationError("No question generated yet.")
        a, b, c, x = self._last_a, self._last_b, self._last_c, self._last_x
        steps = [
            f"Given: ${a}x + {b} = {c}$",
            f"Subtract {b} from both sides: ${a}x = {c - b}$",
            f"Divide both sides by {a}: $x = {(c - b) // a}$",
            f"Final answer: $x = {x}$"
        ]
        return "\n".join(steps)

class FactoringGenerator:
    """Generates factoring quadratic questions and answers.

    Example::
        gen = FactoringGenerator()
        q, a = gen.generate()
        grade_result = gen.grade(user_answer="(x + 2)(x - 3)")
        solution = gen.worked_solution()
    """
    def __init__(self, min_root: int = -10, max_root: int = 10) -> None:
        self.min_root = min_root
        self.max_root = max_root
        self._last_r1: Optional[int] = None
        self._last_r2: Optional[int] = None
        self._last_b: Optional[int] = None
        self._last_c: Optional[int] = None

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
        self._last_r1 = r1
        self._last_r2 = r2
        self._last_b = b
        self._last_c = c
        question = f"Factor: $x^2 + {b:+}x + {c:+}$"
        answer = f"$(x {r1:+})(x {r2:+})$"
        return question, answer

    def grade(self, user_answer: str) -> Dict[str, Any]:
        """Grade a user's answer for the last generated question.

        Args:
            user_answer: The user's answer as a string (e.g., '(x + 2)(x - 3)').
        Returns:
            Dict with keys: correct (bool), expected (str), user (str), explanation (str)
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if self._last_r1 is None or self._last_r2 is None:
            raise ValidationError("No question generated yet.")
        # Accept either order of roots
        expected_forms = [
            f"(x {'+' if self._last_r1 >= 0 else '-'} {abs(self._last_r1)})(x {'+' if self._last_r2 >= 0 else '-'} {abs(self._last_r2)})",
            f"(x {'+' if self._last_r2 >= 0 else '-'} {abs(self._last_r2)})(x {'+' if self._last_r1 >= 0 else '-'} {abs(self._last_r1)})"
        ]
        user = user_answer.replace(' ', '').replace('$', '')
        expected = [e.replace(' ', '') for e in expected_forms]
        correct = user in expected
        return {
            "correct": correct,
            "expected": expected_forms[0],
            "user": user_answer,
            "explanation": "Correct!" if correct else f"Expected one of: {expected_forms}"
        }

    def worked_solution(self) -> str:
        """Return a step-by-step solution for the last generated question.

        Returns:
            Step-by-step solution as a string.
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if None in (self._last_r1, self._last_r2, self._last_b, self._last_c):
            raise ValidationError("No question generated yet.")
        r1, r2, b, c = self._last_r1, self._last_r2, self._last_b, self._last_c
        steps = [
            f"Given: $x^2 + {b:+}x + {c:+}$",
            f"Find two numbers that multiply to {c} and add to {-(b)}.",
            f"Those numbers are {r1} and {r2}.",
            f"So, $x^2 + {b:+}x + {c:+} = (x {r1:+})(x {r2:+})$"
        ]
        return "\n".join(steps)

class TriangleProblemGenerator:
    """Generates triangle geometry questions and answers (Pythagorean theorem).

    Example::
        gen = TriangleProblemGenerator()
        q, a = gen.generate()
        grade_result = gen.grade(user_answer="5.00")
        solution = gen.worked_solution()
    """
    def __init__(self, min_leg: int = 3, max_leg: int = 20) -> None:
        self.min_leg = min_leg
        self.max_leg = max_leg
        self._last_a: Optional[int] = None
        self._last_b: Optional[int] = None
        self._last_c: Optional[float] = None

    def generate(self) -> Tuple[str, str]:
        """Generate a right triangle problem and its solution.

        Returns:
            Tuple of (question_latex, answer_latex)
        """
        a = random.randint(self.min_leg, self.max_leg)
        b = random.randint(self.min_leg, self.max_leg)
        c = (a ** 2 + b ** 2) ** 0.5
        self._last_a = a
        self._last_b = b
        self._last_c = c
        question = f"Given a right triangle with legs $a={a}$ and $b={b}$, find the hypotenuse $c$."
        answer = f"$c = \\sqrt{{{a}^2 + {b}^2}} = {c:.2f}$"
        return question, answer

    def grade(self, user_answer: str) -> Dict[str, Any]:
        """Grade a user's answer for the last generated question.

        Args:
            user_answer: The user's answer as a string (e.g., '5.00').
        Returns:
            Dict with keys: correct (bool), expected (str), user (str), explanation (str)
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if self._last_c is None:
            raise ValidationError("No question generated yet.")
        try:
            user_val = float(user_answer.strip().replace('$c =', '').replace('c =', '').replace('$', '').strip())
        except Exception:
            return {"correct": False, "expected": f"{self._last_c:.2f}", "user": user_answer, "explanation": "Could not parse answer as float."}
        correct = abs(user_val - self._last_c) < 0.01
        return {
            "correct": correct,
            "expected": f"{self._last_c:.2f}",
            "user": f"{user_val:.2f}",
            "explanation": "Correct!" if correct else f"Expected c = {self._last_c:.2f}"
        }

    def worked_solution(self) -> str:
        """Return a step-by-step solution for the last generated question.

        Returns:
            Step-by-step solution as a string.
        Raises:
            ValidationError: If no question has been generated yet.
        """
        if None in (self._last_a, self._last_b, self._last_c):
            raise ValidationError("No question generated yet.")
        a, b, c = self._last_a, self._last_b, self._last_c
        steps = [
            f"Given: right triangle with legs $a={a}$ and $b={b}$.",
            f"Use the Pythagorean theorem: $c = \\sqrt{{a^2 + b^2}}$.",
            f"Plug in values: $c = \\sqrt{{{a}^2 + {b}^2}}$.",
            f"Calculate: $c = \\sqrt{{{a**2} + {b**2}}} = {c:.2f}$",
            f"Final answer: $c = {c:.2f}$"
        ]
        return "\n".join(steps)

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
