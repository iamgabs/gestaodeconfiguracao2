# GESTAO 2

## Como executar? 

~~~bash
# clonar o repositório
git clone https://github.com/iamgabs/gestaodeconfiguracao2.git

# criar ambiente virutal (linux)
python3 -m venv venv

# ativar ambiente virtual
source ./venv/bin/activate

# fazer o download das bibliotecas
pip install -r requirements.txt 

# entrar em src
cd ./src

# executar o app
flask --app ./app.py run
~~~


## Sobre

Escolhi usar o workflow "git lab", pois na maioria dos projetos que já atuei,
era o padrão mais utilizado e a níveis organizacionais, é melhor que o padrão "github". 
