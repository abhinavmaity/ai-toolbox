# Contributing to AI Toolbox

Thank you for your interest in contributing! Please see our [Contributing Guide](docs/contributing.md) for detailed information.

## Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/abhinavmaity-fi/ai-toolbox.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Install dev dependencies: `pip install -e ".[dev]"`
5. Make your changes
6. Run tests: `pytest`
7. Commit: `git commit -m "feat: your feature"`
8. Push: `git push origin feature/your-feature`
9. Create a Pull Request

## Code Quality

Before submitting:

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/

# Run tests
pytest --cov=ai_toolbox
```

## Questions?

Open an issue or check our [documentation](docs/contributing.md) for more details.

