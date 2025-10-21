# Contributing to AI Toolbox

Thank you for your interest in contributing to AI Toolbox! This document provides guidelines and instructions for contributing.

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/yourusername/ai-toolbox.git
cd ai-toolbox
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks (optional but recommended)
pre-commit install
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add type hints to all functions
- Write docstrings for all public APIs

### 3. Add Tests

All new features must include tests:

```python
# tests/test_your_feature.py
def test_your_feature():
    """Test description."""
    # Your test code
    assert result == expected
```

### 4. Run Tests and Checks

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=ai_toolbox --cov-report=html

# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Code Style

### Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use [Black](https://black.readthedocs.io/) for formatting (line length: 88)
- Use [Ruff](https://docs.astral.sh/ruff/) for linting
- Maximum line length: 88 characters

### Type Hints

Always include type hints:

```python
from typing import List, Optional

def process_items(
    items: List[str],
    threshold: Optional[float] = None
) -> List[str]:
    """Process a list of items."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    More detailed description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ValueError: When parameter is invalid.
    """
    ...
```

## Testing Guidelines

- Write tests for all new functionality
- Aim for >80% code coverage
- Use descriptive test names
- Include both positive and negative test cases
- Use fixtures for common test data (in `conftest.py`)

Example:

```python
import pytest
from ai_toolbox import AIToolbox


def test_initialization_with_config():
    """Test that AIToolbox initializes correctly with config."""
    config = {"key": "value"}
    toolbox = AIToolbox(config=config)
    assert toolbox.config == config


def test_initialization_without_config():
    """Test that AIToolbox initializes with empty config by default."""
    toolbox = AIToolbox()
    assert toolbox.config == {}
```

## Documentation

- Update documentation for any API changes
- Add examples for new features
- Update CHANGELOG.md

## Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Add your changes to CHANGELOG.md under "Unreleased"
4. Fill out the pull request template
5. Wait for review from maintainers
6. Address any requested changes

## Code Review

All submissions require review. We may ask you to:

- Make changes to code style
- Add or modify tests
- Update documentation
- Clarify commit messages

## Questions?

If you have questions:

- Check existing issues on GitHub
- Ask in the pull request discussion
- Open a new issue for discussion

Thank you for contributing! 🎉

