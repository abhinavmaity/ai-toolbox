# AI Toolbox

[![PyPI version](https://badge.fury.io/py/ai-toolbox.svg)](https://badge.fury.io/py/ai-toolbox)
[![Python Versions](https://img.shields.io/pypi/pyversions/ai-toolbox.svg)](https://pypi.org/project/ai-toolbox/)
[![Tests](https://github.com/abhinavmaity/ai-toolbox/workflows/Tests/badge.svg)](https://github.com/abhinavmaity/ai-toolbox/actions)
[![codecov](https://codecov.io/gh/abhinavmaity/ai-toolbox/branch/main/graph/badge.svg)](https://codecov.io/gh/abhinavmaity/ai-toolbox)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive AI toolbox for developers providing essential utilities and tools for AI/ML projects.

## Features

- 🚀 Easy to use API
- 🔧 Modular and extensible design
- 📦 Minimal dependencies
- 🎯 Type-safe with full type hints
- 📚 Comprehensive documentation
- ✅ Well-tested with high coverage

## Installation

Install from PyPI:

```bash
pip install ai-toolbox
```

For development:

```bash
pip install ai-toolbox[dev]
```

## Quick Start

```python
from ai_toolbox import AIToolbox

# Initialize the toolbox
toolbox = AIToolbox(config={"option1": "value1"})

# Use the toolbox
data = [1, 2, 3, 4, 5]
result = toolbox.process(data)
print(result)
```

## Documentation

Full documentation is available at [https://ai-toolbox.readthedocs.io](https://ai-toolbox.readthedocs.io)

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/abhinavmaity/ai-toolbox.git
cd ai-toolbox

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_toolbox --cov-report=html

# Run specific test file
pytest tests/test_core.py
```

### Code Quality

```bash
# Format code with Black
black src/ tests/

# Lint with Ruff
ruff check src/ tests/

# Type check with mypy
mypy src/
```

### Building

```bash
# Install build tools
pip install build

# Build the package
python -m build

# The built files will be in dist/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to:
- Add tests for any new features
- Update documentation as needed
- Follow the existing code style
- Ensure all tests pass

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Abhinav Maity** - *Initial work* - [abhinavmaity](https://github.com/abhinavmaity)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## Support

If you have any questions or issues, please open an issue on [GitHub](https://github.com/abhinavmaity/ai-toolbox/issues).

