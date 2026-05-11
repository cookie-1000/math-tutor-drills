#!/usr/bin/env python3
"""Basic usage example for math_tutor_drills."""

from math_tutor_drills import MathTutorDrills, MathTutorDrillsOptions


def main() -> None:
    # Create with default options
    instance = MathTutorDrills()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = MathTutorDrillsOptions(verbose=True)
    instance = MathTutorDrills(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
