"""
Pytest configuration and fixtures.

This file contains shared fixtures and configuration for all tests.
"""

import pytest


@pytest.fixture
def sample_config():
    """Provide a sample configuration for tests."""
    return {
        "option1": "value1",
        "option2": "value2",
    }


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]

