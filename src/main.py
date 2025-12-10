import click
import os
from src.prompts import get_network_variables
from src.generator import generate_project

@click.group()
def cli():
    """MSP Scaffolder: Standardize your deployments."""
    pass

@click.command()
def new_network():
    """Scaffold a new Azure Network project."""
    
    # 1. Gather Inputs
    click.clear()
    click.secho("🚀 Starting new Azure Network Scaffold...", fg="green", bold=True)
    variables = get_network_variables() 
    
    # 2. Generate Files
    try:
        output_path, files = generate_project("azure-network", variables)
        
        # 3. Success Message
        click.secho("\n✅ Success! Project Scaffolded.", fg="green", bold=True)
        click.echo(f"📂 Location: {output_path}")
        click.echo("📄 Files Generated:")
        for f in files:
            click.echo(f"   - {f}")
            
    except Exception as e:
        click.secho(f"\n❌ Error: {e}", fg="red")

# Register the command
cli.add_command(new_network)

if __name__ == '__main__':
    cli()
