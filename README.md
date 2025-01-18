# delete-repo

### 

1. Gere um **Personal Access Token** no GitHub com permissão para excluir repositórios:
    - Vá até **Settings > Developer settings > Personal Access Tokens > Tokens classic**.
    - Gere um token com a permissão `delete_repo`.
2. Substitua os valores em `GITHUB_TOKEN` e `USERNAME` no script pelo seu token e nome de usuário.
3. Execute o script para apagar os repositórios da lista.
4. Caso queira manter o script usando o token com o dotenv, crie um arquivo .env com o GITHUB_TOKEN recebendo o valor do seu token. 