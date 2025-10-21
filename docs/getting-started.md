# Getting Started

This guide will help you get started with AI Toolbox.

## Installation

### From PyPI (Recommended)

Install the latest stable version from PyPI:

```bash
pip install ai-toolbox
```

### Development Installation

For development, clone the repository and install in editable mode:

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-toolbox.git
cd ai-toolbox

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## Requirements

- Python 3.9 or higher
- pip (Python package installer)

## Your First Program

Create a new Python file and try this simple example:

```python
from ai_toolbox import AIToolbox

# Initialize the toolbox
toolbox = AIToolbox()

# Process some data
data = [1, 2, 3, 4, 5]
result = toolbox.process(data)

print(f"Processed: {result}")
```

## Configuration

AI Toolbox can be configured with a dictionary:

```python
from ai_toolbox import AIToolbox

config = {
    "option1": "value1",
    "option2": "value2",
}

toolbox = AIToolbox(config=config)
```

## Using Utilities

The library includes utility functions:

```python
from ai_toolbox.utils import validate_config, format_output

# Validate a configuration
config = {"key": "value"}
is_valid = validate_config(config)

# Format output
result = format_output({"result": "success"})
```

## Next Steps

- Check out more [Examples](examples.md)
- Read the [API Reference](api.md)
- Learn about [Contributing](contributing.md)

## Getting Help

If you need help:

1. Check the [documentation](index.md)
2. Look at the [examples](examples.md)
3. Search [existing issues](https://github.com/yourusername/ai-toolbox/issues)
4. Create a new issue if needed

## Common Issues

### Import Error

If you get an import error, make sure you've installed the package:

```bash
pip install ai-toolbox
```

### Type Hints Not Working

Make sure you're using Python 3.9 or higher:

```bash
python --version
```

## What's Next?

Now that you have AI Toolbox installed:

- Explore the [Examples](examples.md) page
- Read the [API Reference](api.md)
- Consider [Contributing](contributing.md) to the project

