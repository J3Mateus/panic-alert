# README - PANIC ALERT

Este é um guia passo a passo para configurar backend do PANIC ALERT, desde a criação de um ambiente virtual até a execução do projeto.

## Passo 1: Pré-requisitos

Certifique-se de que você tenha os seguintes pré-requisitos instalados em seu sistema:

- Docker
- Python 3.x (recomendado)
- Git (opcional, mas útil para controle de versão)
- Django (é recomendável usar a versão mais recente)

## Passo 2: Configurando o Ambiente Virtual (venv)

É uma prática recomendada criar um ambiente virtual para o seu projeto, a fim de isolar as dependências. Siga as etapas abaixo para configurar o ambiente virtual:

1. Abra o terminal e navegue até a pasta raiz do seu projeto.

2. Execute o seguinte comando para criar um ambiente virtual (substitua 'nome_venv' pelo nome que você deseja dar ao seu ambiente virtual):

   ```shell
   python -m venv nome_venv
3. Ative o ambiente virtual. No Windows, execute:

   ```shell
    nome_venv\Scripts\activate

4. No macOS e Linux, execute:

   ```shell
   source nome_venv/bin/activate
## Passo 3: Instalando Requisitos

Após configurar o ambiente virtual, você pode instalar as dependências do projeto. Certifique-se de estar com o ambiente virtual ativado. Execute o seguinte comando na raiz do seu projeto para instalar os requisitos do projeto:
1. Abra o terminal e navegue até a pasta raiz do seu projeto.
   ```shell
     pip install -r requirements/requirements.txt
      
## Passo 4: Configurando o arquivo .env
1. Crie um arquivo chamado .env na raiz do seu projeto.
  ```env
    DJANGO_DATABASE_URL="postgres://postgres:1234@localhost:5432/school-alert"
    DJANGO_BASE_BACKEND_URL=http://localhost:8000
    BASE_FRONTEND_URL=http://localhost:3000
    CORS_ORIGIN_WHITELIST=["*"]
    
    DOCKER_VOLUME_APP=.
    DOCKER_VOLUME_DOCKER=./docker
    DOCKER_VOLUME_STATIC=./run/static
    DOCKER_VOLUME_MEDIA=./run/media
    
    DOCKER_PROJECT_NAME=alerta-escolar
    DOCKER_NGINX_PORT=8000
   ```
## Passo 5: Configurando o Banco de Dados

1. Abra o terminal e navegue até a pasta raiz do seu projeto.
   ```shell
    python manage.py migrate
