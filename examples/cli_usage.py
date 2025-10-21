"""
Example of using the AI Toolbox CLI programmatically.

This example shows how to invoke CLI commands from Python code.
"""

from click.testing import CliRunner
from ai_toolbox.main import cli


def main():
    """Demonstrate CLI usage from Python code."""
    print("AI Toolbox - CLI Usage Example")
    print("=" * 50)
    
    # Create a CLI runner
    runner = CliRunner()
    
    # Example 1: Get help for the CLI
    print("\n1. CLI Help:")
    result = runner.invoke(cli, ["--help"])
    print(result.output)
    
    # Example 2: Run the hello command
    print("\n2. Running 'hello' command:")
    result = runner.invoke(cli, ["hello"])
    print(result.output)
    
    # Example 3: Check exit codes
    print("\n3. Checking command exit codes:")
    result = runner.invoke(cli, ["hello"])
    print(f"   Exit code: {result.exit_code}")
    print(f"   Success: {result.exit_code == 0}")
    
    print("\n" + "=" * 50)
    print("Example completed successfully!")
    print("\nTo use the CLI from the command line, install the package and run:")
    print("  ai-toolbox --help")
    print("  ai-toolbox hello")


if __name__ == "__main__":
    main()

