"""Type definitions for math_tutor_drills."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class MathTutorDrillsOptions:
    """Configuration options for MathTutorDrills.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Template-driven question generators (linear equations, factoring, triangles)
        feature_2: Configuration for: LaTeX/Overleaf-ready export with randomized variants
        feature_3: Configuration for: Auto-grading with step-checkable final answers and worked-solution outlines
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None


@dataclass
class MathTutorDrillsResult:
    """Result returned by MathTutorDrills operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
