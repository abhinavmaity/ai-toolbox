"""
Tests for utility functions.
"""

import pytest
from ai_toolbox.utils import validate_config, format_output


def test_validate_config_valid(sample_config):
    """Test validate_config with valid config."""
    assert validate_config(sample_config) is True


def test_validate_config_invalid():
    """Test validate_config with invalid config."""
    assert validate_config("not a dict") is False


def test_format_output():
    """Test format_output function."""
    result = format_output({"key": "value"})
    assert isinstance(result, str)
    assert "key" in result

