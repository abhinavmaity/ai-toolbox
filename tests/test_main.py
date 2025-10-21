"""
Tests for the CLI module.
"""

from click.testing import CliRunner
from ai_toolbox.main import cli, hello


def test_cli_group():
    """Test that the CLI group exists and is callable."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "AI Toolbox" in result.output


def test_hello_command():
    """Test the hello command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert "Hello from the AI Toolbox" in result.output


def test_hello_command_directly():
    """Test the hello command invoked directly."""
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert "Hello from the AI Toolbox" in result.output

