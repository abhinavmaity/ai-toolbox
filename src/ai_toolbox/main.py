"""
Command-line interface for AI Toolbox.

This module provides the CLI commands for interacting with the AI Toolbox.
"""

import os

import click
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()


@click.group()
def cli():
    """AI Toolbox - A comprehensive AI toolbox for developers."""
    pass


@click.command()
def hello():
    """Print a greeting message from the AI Toolbox."""
    try:
        # Generate a dynamic greeting using LiteLLM with streaming
        response = completion(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Generate a friendly and creative greeting message for the AI Toolbox CLI tool.",
                },
                {
                    "role": "user",
                    "content": "Generate a brief, enthusiastic greeting message (1-2 sentences) for someone using the AI Toolbox.",
                },
            ],
            api_key=os.getenv("OPENAI_API_KEY"),
            stream=True,
        )
        
        # Stream and print the response chunk by chunk
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                click.echo(content, nl=False)
        
        # Add a newline at the end
        click.echo()
    except Exception as e:
        click.echo(f"Error generating greeting: {str(e)}", err=True)
        click.echo("Hello from the AI Toolbox (fallback message)")


cli.add_command(hello)

if __name__ == "__main__":
    cli()

