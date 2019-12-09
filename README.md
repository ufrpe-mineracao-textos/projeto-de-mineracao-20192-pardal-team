<h1 align="center">Pardal Team</h1>
<p align="center">Análise de Sentimentos em Tweets</p>

## Descrição

Pardal é uma simples aplicação para análise, em tempo real, de sentimentos em Tweets buscados por palavra-chave. Os resultados obtidos são exibidos em um dashboard de fácil entendimento onde cada Tweets é categorizado como positivo, neutro ou negativo.

## Equipe

- [Abílio Nogueira](https://github.com/AbilioNB)
- [Edilson Alves](https://github.com/edilsonalves)

## Execução

Para executar a aplicação é necessário possuir uma conta de desenvolvedor no Twitter, o objetivo é gerar as chaves e tokens necessários para comunicação com a API oficial da plataforma.

<p align="center">
  <img src="./images/01.png">
</p>

### Passos

Clonar repositório:

`$ git clone https://github.com/ufrpe-mineracao-textos/projeto-de-mineracao-20192-pardal-team.git`

Acessar diretório:

`$ cd projeto-de-mineracao-20192-pardal-team/pardal/application`

Criar arquivo .env:

`$ touch .env`

Criar variáveis de ambiente com as chaves e tokens gerados (arquivo .env):

```
CONSUMER_KEY=INSERIR_API_KEY
CONSUMER_SECRET=INSERIR_API_SECRET_KEY
ACCESS_TOKEN=INSERIR_ACCESS_TOKEN
ACCESS_TOKEN_SECRET=INSERIR_ACCESS_TOKEN_SECRET
```

Criar ambiente virtual:

`$ python -m venv .venv`

Ativar ambiente virtual:

`$ source .venv/bin/activate`

Instalar dependências:

`$ pip install -r requirements.txt`

Executar aplicação:

`$ python app.py`

Acessar aplicação:

`http://127.0.0.1:5000`
