"""
Tests for core functionality.
"""

import pytest
from ai_toolbox.core import AIToolbox


def test_aitoolbox_init():
    """Test AIToolbox initialization."""
    toolbox = AIToolbox()
    assert toolbox.config == {}


def test_aitoolbox_init_with_config(sample_config):
    """Test AIToolbox initialization with config."""
    toolbox = AIToolbox(config=sample_config)
    assert toolbox.config == sample_config


def test_process(sample_data):
    """Test process method."""
    toolbox = AIToolbox()
    result = toolbox.process(sample_data)
    assert result == sample_data

