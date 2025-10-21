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


def test_hello_command(mocker):
    """Test the hello command with mocked LiteLLM streaming completion."""
    # Create mock streaming chunks that mimic LiteLLM's streaming response structure
    mock_chunks = [
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="Hello "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="from "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="the "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="AI "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="Toolbox! "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="This "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="is "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="a "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="test "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="greeting."))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content=None))]),  # End of stream
    ]
    
    # Mock the completion function to return an iterator of chunks
    mock_completion = mocker.patch("ai_toolbox.main.completion", return_value=iter(mock_chunks))
    
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    
    assert result.exit_code == 0
    assert "Hello from the AI Toolbox! This is a test greeting." in result.output
    
    # Verify that completion was called with the correct parameters including stream=True
    mock_completion.assert_called_once()
    call_args = mock_completion.call_args
    assert call_args.kwargs["model"] == "gpt-4o-mini"
    assert call_args.kwargs["stream"] is True
    assert len(call_args.kwargs["messages"]) == 2
    assert call_args.kwargs["messages"][0]["role"] == "system"
    assert call_args.kwargs["messages"][1]["role"] == "user"


def test_hello_command_directly(mocker):
    """Test the hello command invoked directly with mocked streaming completion."""
    # Create mock streaming chunks
    mock_chunks = [
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="Welcome "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="to "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="AI "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="Toolbox "))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content="testing!"))]),
        mocker.Mock(choices=[mocker.Mock(delta=mocker.Mock(content=None))]),
    ]
    
    # Mock the completion function to return an iterator
    mocker.patch("ai_toolbox.main.completion", return_value=iter(mock_chunks))
    
    runner = CliRunner()
    result = runner.invoke(hello)
    
    assert result.exit_code == 0
    assert "Welcome to AI Toolbox testing!" in result.output


def test_hello_command_with_api_error(mocker):
    """Test the hello command when the API call fails."""
    # Mock the completion function to raise an exception
    mocker.patch("ai_toolbox.main.completion", side_effect=Exception("API Error"))
    
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    
    assert result.exit_code == 0
    assert "Error generating greeting: API Error" in result.output
    assert "Hello from the AI Toolbox (fallback message)" in result.output

