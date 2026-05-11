# math_tutor_drills

Generate and grade algebra/geometry drill sets with LaTeX and answer keys.

## Installation

```bash
pip install math_tutor_drills
```

## Quick Start

```python
from math_tutor_drills import MathTutorDrills

instance = MathTutorDrills()
result = instance.run()
print(result)
```

## Features

- Template-driven question generators (linear equations, factoring, triangles)
- LaTeX/Overleaf-ready export with randomized variants
- Auto-grading with step-checkable final answers and worked-solution outlines

## API Reference

### `MathTutorDrills`

#### Constructor

```python
MathTutorDrills(options: MathTutorDrillsOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `MathTutorDrillsResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/math_tutor_drills/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
