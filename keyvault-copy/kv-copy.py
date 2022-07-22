from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import subprocess
secret_list = []
name_list = []

# Entries
Source_KeyVault = ""
Destination_KeyVault = ""


# Create a SecretClient using default Azure Credentials
credential = DefaultAzureCredential()
src_vault_url = Source_KeyVault
src_secret_client = SecretClient(src_vault_url, credential)
secrets = src_secret_client.list_properties_of_secrets()

for secret in secrets:
    name_list.append(secret.name)

    if secret.enabled == True:
        secret_value = src_secret_client.get_secret(secret.name)
        secret_list.append(secret_value.value)

# Copy Secret on Destination Keyvault resource
target_vault_url = Destination_KeyVault
target_secret_client = SecretClient(target_vault_url, credential)

for i, j in zip(name_list, secret_list):
    print(f"{i}:{j}")
    target_secret_client.set_secret(i, j)
