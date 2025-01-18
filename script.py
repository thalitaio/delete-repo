import requests
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "thalitaio"

repositories_to_delete = ["desafio02"]

for repo in repositories_to_delete:
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"Repositório '{repo}' apagado com sucesso!")
    else:
        print(f"Falha ao apagar o repositório '{repo}': {response.status_code}, {response.text}")
