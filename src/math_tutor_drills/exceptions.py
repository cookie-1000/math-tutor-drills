"""Custom exceptions for math_tutor_drills."""

from __future__ import annotations


class MathTutorDrillsError(Exception):
    """Base exception for all MathTutorDrills errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(MathTutorDrillsError):
    """Raised when the SDK is misconfigured."""


class ValidationError(MathTutorDrillsError):
    """Raised when input validation fails."""


class TimeoutError(MathTutorDrillsError):
    """Raised when an operation exceeds its time limit."""
