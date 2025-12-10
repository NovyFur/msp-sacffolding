import click
from src.prompts import get_network_variables
from src.generator import generate_project
# IMPORT THE NEW MODULE
from src.deployer import deploy_terraform 

@click.group()
def cli():
    """MSP Scaffolder: Standardize your deployments."""
    pass

@click.command()
def new_network():
    """Scaffold a new Azure Network project."""
    
    click.clear()
    click.secho("🚀 Starting new Azure Network Scaffold...", fg="green", bold=True)
    variables = get_network_variables() 
    
    try:
        output_path, files = generate_project("azure-network", variables)
        
        click.secho("\n✅ Success! Project Scaffolded.", fg="green", bold=True)
        click.echo(f"📂 Location: {output_path}")
        
        # --- NEW SECTION: ASK TO DEPLOY ---
        if click.confirm("\n🚀 Would you like to deploy this to Azure right now?"):
            deploy_terraform(output_path)
        # ----------------------------------
            
    except Exception as e:
        click.secho(f"\n❌ Error: {e}", fg="red")

cli.add_command(new_network)

if __name__ == '__main__':
    cli()
