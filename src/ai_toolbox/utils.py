"""
Utility functions for AI Toolbox.

This module contains helper functions used throughout the library.
"""

from typing import Any, Dict


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration dictionary.

    Args:
        config: Configuration dictionary to validate.

    Returns:
        True if valid, False otherwise.
    """
    # Placeholder implementation
    return isinstance(config, dict)


def format_output(data: Any) -> str:
    """
    Format output data as string.

    Args:
        data: Data to format.

    Returns:
        Formatted string representation.
    """
    return str(data)

