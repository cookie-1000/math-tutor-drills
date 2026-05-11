"""Tests for math_tutor_drills."""

from math_tutor_drills import MathTutorDrills, MathTutorDrillsOptions


class TestMathTutorDrills:
    def test_create_instance_with_defaults(self) -> None:
        instance = MathTutorDrills()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = MathTutorDrillsOptions(verbose=True)
        instance = MathTutorDrills(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = MathTutorDrills()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = MathTutorDrills()
        result = instance.run()
        assert result.error is None
