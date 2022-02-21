# SAPRON-PMS-WEB
Repositório para criação do PMS Web da Seazone em parceria com a Coderockr

## Requisitos para rodar o projeto

- Docker
- Docker Compose
- Make - `opcional somente para facilitar rodar os comandos`

### Setup

- Subir todos os containers: `sudo make setup` ou `./cli/setup`

Esse comando rodará um script bash que vai criar a estrutura das variáveis nos arquivos `.env` do projeto e subir os containers.

Apenas com esse comando, seu projeto deve estar rodando com sucesso localmente.

Obs: Algumas variáveis de ambiente estão com valores que não são reais pois estes não podem ser expostos no repositório remoto.
Para utilizar algumas funcionalidades, como popular o banco de dados local, será necessário falar com algum administrador do projeto para que
os dados reais sejam fornecidos.

Por padrão está configurado para acessar a API em ambiente local na porta 8000, mudar 
porta de acordo com a porta usado no backend

``` enviroment
REACT_APP_URL=http://localhost:8000
```

Para acessar o ambiente de homologoção mudar a url da variável **REACT_APP_URL**
para **https://api.staging.sapron.com.br** após feito o processo

É preciso subir novamente o container novamente
``` enviroment
REACT_APP_URL=https://api.staging.sapron.com.br
```

___________
## Backend

O backend foi desenvolvimento usando:

- Docker
- Python3
- Django
- Django Rest Framework

## Documentação dos endpoints
    - Acessar o swagger: `{insira aqui a url do servidor}/swagger/`

### Comandos (executados dentro do diretório root do projeto)
## Ambiente de Desenvolvimento
- Criar ambiente virtual: `python3 -m venv .venv`
- Ativar o ambiente virtual: `source .venv/bin/activate`
- Instalar os pacotes: `pip install -r backend/requirements-dev.txt`
- Rodar o linter flake8: `python3 -m flake8`
- Subir apenas o container do back end: `make docker-backend`

- **database**
    - Gerar migrations: `make migrate-generate`
    - Rodar migrations: `make migrate-run`
    - Apagar todos os dados do db: `./cli/python manage.py flush`
    - Popular várias* tabelas do bd: `./cli/python manage.py filler`
    - Criar um usuário root: `./cli/python manage.py createsuperuser`

    * A função só funciona como esperado se o desenvolvedor possuir as chaves do bucket da S3 no arquivo .env dentro da pasta backend. As chaves estão disponíveis na documentação do Channel Manager.
    
    ATENÇÃO: somente usar a função que popula o bd se todos os dados tiverem sido apagados com a função que limpa o bd
___________
## Frontend
O frontend foi desenvolvido usando:

- React
- Material UI

Para rodar os comandos de yarn dentro do container usar `./cli/yarn <comando>`

### Comandos
- Subir apenas o container do frontend (dentro do diretório root): `make docker-front`

Comandos de dentro do diretório 'front':

- Subir um servidor do storybook: `yarn storybook`
- Rodar o lint: `yarn lint`
- Rodar o lint e fixar erros: `yarn lint:fix`
- Gera templates tanto de view com componente: `yarn template`
- Abre o cypress: `yarn cypress`

## Branches e Deploy

Esse projeto usa uma versão modificada do [Git Flow](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow).

Todo novo desenvolvimento (feature) deve ser iniciado em cima da branch `main`, uma vez que o desenvolvimento esteja a ponto de ser revisado, deve ser aberto um pull request para a branch `main` para integrar o desenvolvimento.

Quando as alterações na `main` estiverem estáveis suficiente para serem testadas, deve ser feito um merge da `main` na branch `staging`, feito o merge um workflow automatizado no [Circle CI](https://app.circleci.com/pipelines/github/cabfersp/sapron-pms-web) irão iniciar o build e deploy da aplicação e estarão disponíveis para testes em:

* Frontend: https://staging.sapron.com.br
* Backend: https://api.staging.sapron.com.br

Concluídos os testes e eventuais correções necessárias, deve ser feito um merge da `staging` para a branch `production`, deve forma semelhante quando um workflow no Circle CI irá automaticamente executar o build e deploy da nova versão da aplicação. Após concluído o workflow as alterações estarão disponíveis em:

* Frontend: https://sapron.com.br
* Backend: https://api.sapron.com.br
