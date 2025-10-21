# Examples

This page contains practical examples of using AI Toolbox in various scenarios.

## Basic Usage

### Initializing the Toolbox

```python
from ai_toolbox import AIToolbox

# Initialize with default configuration
toolbox = AIToolbox()

# Initialize with custom configuration
config = {
    "option1": "value1",
    "option2": "value2",
}
toolbox = AIToolbox(config=config)
```

### Processing Data

```python
from ai_toolbox import AIToolbox

toolbox = AIToolbox()
data = [1, 2, 3, 4, 5]
result = toolbox.process(data)
print(result)  # [1, 2, 3, 4, 5]
```

## Using Utilities

### Validating Configuration

```python
from ai_toolbox.utils import validate_config

config = {
    "option1": "value1",
    "option2": "value2",
}

if validate_config(config):
    print("Configuration is valid!")
else:
    print("Invalid configuration")
```

### Formatting Output

```python
from ai_toolbox.utils import format_output

data = {"result": "success", "value": 42}
formatted = format_output(data)
print(formatted)
```

## Advanced Examples

### Custom Configuration

```python
from ai_toolbox import AIToolbox

# Create a custom configuration
config = {
    "max_iterations": 100,
    "threshold": 0.95,
    "verbose": True,
}

# Initialize with configuration
toolbox = AIToolbox(config=config)

# Access configuration
print(toolbox.config["max_iterations"])  # 100
```

### Error Handling

```python
from ai_toolbox import AIToolbox
from ai_toolbox.utils import validate_config

try:
    config = {"option": "value"}
    
    if not validate_config(config):
        raise ValueError("Invalid configuration")
    
    toolbox = AIToolbox(config=config)
    result = toolbox.process([1, 2, 3])
    
except ValueError as e:
    print(f"Error: {e}")
```

## Complete Example

Here's a complete example combining multiple features:

```python
from ai_toolbox import AIToolbox
from ai_toolbox.utils import validate_config, format_output


def main():
    # Setup configuration
    config = {
        "option1": "value1",
        "option2": "value2",
    }
    
    # Validate configuration
    if not validate_config(config):
        print("Invalid configuration!")
        return
    
    # Initialize toolbox
    toolbox = AIToolbox(config=config)
    
    # Process data
    input_data = [1, 2, 3, 4, 5]
    result = toolbox.process(input_data)
    
    # Format and display output
    formatted_result = format_output(result)
    print(f"Result: {formatted_result}")


if __name__ == "__main__":
    main()
```

For more examples, check out the [examples](https://github.com/abhinavmaity/ai-toolbox/tree/main/examples) directory in the repository.

