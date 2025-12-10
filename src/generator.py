import os
from jinja2 import Environment, FileSystemLoader
import click

def generate_project(template_name, variables):
    # 1. Setup paths
    # We assume this script is running from the root of the project
    base_dir = os.getcwd()
    template_dir = os.path.join(base_dir, "templates", template_name)
    
    # Create a clean folder name (e.g., "acme_corp-azure-network")
    client_slug = variables['client_name'].replace(" ", "_").lower()
    output_folder_name = f"{client_slug}-{template_name}"
    output_dir = os.path.join(base_dir, "output", output_folder_name)

    # 2. Initialize Jinja2 Environment
    if not os.path.exists(template_dir):
        raise FileNotFoundError(f"Template directory not found: {template_dir}")
        
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # 3. Create Output Directory
    os.makedirs(output_dir, exist_ok=True)

    # 4. Render Files
    files_created = []
    for template_file in env.list_templates():
        # Load and Render
        template = env.get_template(template_file)
        rendered_content = template.render(variables)
        
        # Determine output filename (remove .j2 extension)
        output_filename = template_file.replace(".j2", "")
        output_path = os.path.join(output_dir, output_filename)
        
        # Write file
        with open(output_path, "w") as f:
            f.write(rendered_content)
        
        files_created.append(output_filename)
            
    return output_dir, files_created
