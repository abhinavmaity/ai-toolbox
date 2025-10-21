"""
AI Toolbox - A comprehensive AI toolbox for developers.

This package provides various AI utilities and tools.
"""

__version__ = "0.1.0"
__author__ = "Abhinav Maity"
__email__ = "abhinav.maity2003@gmail.com"

# Import main classes/functions here for easier access
from .core import AIToolbox
from .main import cli
from .utils import validate_config, format_output

__all__ = [
    "__version__",
    "AIToolbox",
    "cli",
    "validate_config",
    "format_output",
]

