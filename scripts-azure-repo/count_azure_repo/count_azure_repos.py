import requests
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Configurações (substitua com seus dados reais no .env)
devops_organization = "sua-organizacao"  # Exemplo: 'minhaempresa'
devops_project = "meu-projeto"           # Exemplo: 'plataforma-devops'
personal_access_token = os.getenv("AZURE_DEVOPS_PAT")

def contar_repositorios(organization: str, project: str, pat: str):
    """
    Conta o número de repositórios Git em um projeto do Azure DevOps.

    Args:
        organization (str): Nome da organização no Azure DevOps.
        project (str): Nome do projeto dentro da organização.
        pat (str): Personal Access Token (PAT) para autenticação.

    Returns:
        None: Apenas imprime o total de repositórios.
    """
    url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=7.1-preview.1"
    headers = {"Content-Type": "application/json"}
    
    response = requests.get(url, auth=("Basic", pat), headers=headers)
    
    # Verifica se a requisição foi bem-sucedida    
    if response.status_code == 200:
        data = response.json()
        total_repos = len(data.get("value", []))
        print(f"O projeto '{project}' tem {total_repos} repositórios.")
    else:
        print(f"Erro ao buscar repositórios: {response.status_code} - {response.text}")

# Executa a função
if __name__ == "__main__":
    if not personal_access_token:
        print("Erro: AZURE_DEVOPS_PAT não definido no arquivo .env")
    else:
        contar_repositorios(devops_organization, devops_project, personal_access_token)
