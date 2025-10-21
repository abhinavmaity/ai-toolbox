# API Reference

## Core Module

### AIToolbox

Main class for AI Toolbox functionality.

```python
from ai_toolbox import AIToolbox
```

#### `__init__(config: Optional[Dict[str, Any]] = None)`

Initialize the AI Toolbox.

**Parameters:**
- `config` (Optional[Dict[str, Any]]): Optional configuration dictionary.

**Example:**
```python
toolbox = AIToolbox(config={"option1": "value1"})
```

#### `process(data: List[Any]) -> List[Any]`

Process input data.

**Parameters:**
- `data` (List[Any]): Input data to process.

**Returns:**
- `List[Any]`: Processed data.

**Example:**
```python
data = [1, 2, 3, 4, 5]
result = toolbox.process(data)
```

## Utilities Module

### validate_config

Validate configuration dictionary.

```python
from ai_toolbox.utils import validate_config
```

**Parameters:**
- `config` (Dict[str, Any]): Configuration dictionary to validate.

**Returns:**
- `bool`: True if valid, False otherwise.

**Example:**
```python
config = {"option1": "value1"}
is_valid = validate_config(config)
```

### format_output

Format output data as string.

```python
from ai_toolbox.utils import format_output
```

**Parameters:**
- `data` (Any): Data to format.

**Returns:**
- `str`: Formatted string representation.

**Example:**
```python
result = format_output({"key": "value"})
```

## Type Definitions

The library uses Python's type hints for better IDE support and type safety. Import types from the `typing` module as needed:

```python
from typing import Any, Dict, List, Optional
```

