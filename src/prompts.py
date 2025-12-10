import click
import datetime

def get_network_variables():
    """Asks the user for specific network inputs."""
    vars = {}
    
    click.secho("\n--- 📋 CLIENT DETAILS ---", fg="cyan")
    vars['client_name'] = click.prompt("Client Name", type=str)
    vars['engineer_name'] = click.prompt("Your Name (Engineer)", type=str)
    vars['deployment_date'] = datetime.date.today().isoformat()
    
    click.secho("\n--- ☁️ AZURE CONFIG ---", fg="cyan")
    vars['location'] = click.prompt("Azure Region", default="East US 2")
    
    click.secho("\n--- 🔌 NETWORK CONFIG ---", fg="cyan")
    # Validator could be added here for IP regex, keeping it simple for now
    vars['vnet_cidr'] = click.prompt("VNet CIDR", default="10.100.0.0/16")
    
    # We will assume a standard topology for this template
    vars['subnets'] = [
        {
            "name": "Management",
            "cidr": click.prompt("Management Subnet CIDR", default="10.100.1.0/24"),
            "purpose": "Jumpboxes, MSP Admin Tools"
        },
        {
            "name": "Servers",
            "cidr": click.prompt("Server Subnet CIDR", default="10.100.10.0/24"),
            "purpose": "Domain Controllers, App Servers"
        }
    ]
    
    vars['vpn_sku'] = click.prompt("VPN Gateway SKU", default="VpnGw1")
    
    return vars
