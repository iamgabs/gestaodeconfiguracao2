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
cd /app/src

# executar o app
FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 flask run

# na vm1 executar
curl http://192.168.56.11:5000/products
~~~


## Sobre

Escolhi usar o workflow "git lab", pois na maioria dos projetos que já atuei,
era o padrão mais utilizado e a níveis organizacionais, é melhor que o padrão "github". 
