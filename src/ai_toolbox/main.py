"""
Command-line interface for AI Toolbox.

This module provides the CLI commands for interacting with the AI Toolbox.
"""

import click


@click.group()
def cli():
    """AI Toolbox - A comprehensive AI toolbox for developers."""
    pass


@click.command()
def hello():
    """Print a greeting message from the AI Toolbox."""
    click.echo("Hello from the AI Toolbox")

cli.add_command(hello)

if __name__ == "__main__":
    cli()

