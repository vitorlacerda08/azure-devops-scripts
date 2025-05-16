# 🧾 Contador de Repositórios do Azure DevOps

Este script em Python acessa a API do Azure DevOps e retorna o número de repositórios Git em um projeto específico.

## 📦 Requisitos

- Python 3.8+
- Um token de acesso pessoal (PAT) do Azure DevOps com permissão de leitura nos repositórios

## ⚙️ Instalação

```bash
git clone https://github.com/vitorlacerda08/azure-devops-scripts.git
cd azure-devops-scripts

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install -r requirements.txt
cp .env.example .env
```

## 🚀 Como usar

Edite `count_azure_repos.py` e configure:

```python
devops_organization = "sua-organizacao"
devops_project = "seu-projeto"
```

Execute o script:

```bash
python count_azure_repos.py
```

## 🔐 Segurança

- O token é carregado via `.env`, que **não deve ser versionado**.
- `.env` já está no `.gitignore` (recomendado).

## 🛠️ Tecnologias utilizadas

- Python
- Azure DevOps REST API
- dotenv
- requests

## 📄 Licença

MIT