Install the libraries:
pip install -r requirements.txt


Run the tool:
python -m src.main new-network


This will trigger the prompts. Once you finish answering, check the newly created output/ folder. You will see a folder named after your client containing the fully written Documentation and Terraform code.


To Do:

Add Backend block to main.tf.j2

terraform {
  backend "azurerm" {
    resource_group_name  = "RG-MSP-INTERNAL-TOOLS"  # Your MSP's RG
    storage_account_name = "stgmspterraform"        # Your MSP's Storage Account
    container_name       = "tfstate"
    key                  = "{{ client_name }}.azure-network.tfstate" # Unique file per client
    use_azuread_auth     = true                     # Secure access
  }
}


HOW TO COMPILE FOR NON-PYTHON USERS:

Install PyInstaller:

pip install pyinstaller


Build the executable:

pyinstaller --onefile --name msp-tool src/main.py



(Note: You will need to configure PyInstaller to include your templates/ folder, as it doesn't pick up non-code files by default. You can do this by adding --add-data "templates;templates" to the command).
