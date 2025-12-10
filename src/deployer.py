import os
import subprocess
import click

def run_command(command, cwd):
    """Runs a shell command and prints the output in real-time."""
    try:
        process = subprocess.Popen(
            command, 
            cwd=cwd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            shell=True
        )
        
        # Stream output to the console so the user sees what's happening
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                
        if process.returncode != 0:
            click.secho(f"❌ Command failed: {command}", fg="red")
            return False
            
        return True
    except Exception as e:
        click.secho(f"❌ Error executing command: {e}", fg="red")
        return False

def deploy_terraform(project_path):
    """Initializes and applies the Terraform configuration."""
    
    click.secho("\n--- 🚀 STARTING AZURE DEPLOYMENT ---", fg="yellow", bold=True)
    
    # 1. Check if user is logged in to Azure
    click.echo("Checking Azure authentication...")
    # This runs 'az account show' to see if we have an active session
    if not run_command("az account show", cwd=project_path):
        click.secho("⚠️ You are not logged in. Please run 'az login' and try again.", fg="red")
        return

    # 2. Terraform Init (Downloads the Azure providers)
    click.secho("\n--- 📦 INITIALIZING TERRAFORM ---", fg="cyan")
    if not run_command("terraform init", cwd=project_path):
        return

    # 3. Terraform Plan (Shows what will be built)
    click.secho("\n--- 📋 PLANNING DEPLOYMENT ---", fg="cyan")
    if not run_command("terraform plan -out=tfplan", cwd=project_path):
        return

    # 4. Terraform Apply (Actually builds it)
    if click.confirm("\n⚠️ Do you want to apply these changes to Azure?", default=False):
        click.secho("\n--- 🏗️ DEPLOYING RESOURCES ---", fg="green", blink=True)
        run_command("terraform apply tfplan", cwd=project_path)
        click.secho("\n✅ Deployment Complete!", fg="green", bold=True)
    else:
        click.echo("Deployment cancelled. Files are saved locally.")
