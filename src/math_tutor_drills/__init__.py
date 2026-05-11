"""
math_tutor_drills - Generate and grade algebra/geometry drill sets with LaTeX and answer keys.
"""

__version__ = "0.1.0"

from .templatedriven_question_genera import MathTutorDrills
from .types import MathTutorDrillsOptions, MathTutorDrillsResult
from .exceptions import MathTutorDrillsError, ConfigurationError, ValidationError

__all__ = [
    "MathTutorDrills",
    "MathTutorDrillsOptions",
    "MathTutorDrillsResult",
    "MathTutorDrillsError",
    "ConfigurationError",
    "ValidationError",
]
