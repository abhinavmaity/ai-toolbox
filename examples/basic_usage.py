"""
Basic usage example for AI Toolbox.

This example demonstrates the basic functionality of the AI Toolbox library.
"""

from ai_toolbox import AIToolbox
from ai_toolbox.utils import validate_config, format_output


def main():
    """Run basic usage examples."""
    print("AI Toolbox - Basic Usage Example")
    print("=" * 50)

    # Example 1: Initialize with default config
    print("\n1. Initialize with default config:")
    toolbox = AIToolbox()
    print(f"   Toolbox config: {toolbox.config}")

    # Example 2: Initialize with custom config
    print("\n2. Initialize with custom config:")
    config = {
        "option1": "value1",
        "option2": "value2",
    }
    toolbox = AIToolbox(config=config)
    print(f"   Toolbox config: {toolbox.config}")

    # Example 3: Validate configuration
    print("\n3. Validate configuration:")
    is_valid = validate_config(config)
    print(f"   Config is valid: {is_valid}")

    # Example 4: Process data
    print("\n4. Process data:")
    data = [1, 2, 3, 4, 5]
    result = toolbox.process(data)
    print(f"   Input: {data}")
    print(f"   Output: {result}")

    # Example 5: Format output
    print("\n5. Format output:")
    formatted = format_output(result)
    print(f"   Formatted: {formatted}")

    print("\n" + "=" * 50)
    print("Example completed successfully!")


if __name__ == "__main__":
    main()

