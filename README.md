# Analysis Log

## Índice
- [Analysis Log](#analysis-log)
  - [Índice](#%C3%ADndice)
  - [Instalar](#instalar)
  - [Instruções](#instru%C3%A7%C3%B5es)
    - [Download](#download)
    - [Arquivos](#arquivos)
    - [Executando o projeto](#executando-o-projeto)
  - [Resultado](#resultado)
  - [Contribuindo](#contribuindo)
  
## Instalar
[Docker Install](https://docs.docker.com/install/)\
[Pipenv Install](https://docs.pipenv.org/en/latest/install/)

## Instruções

### Download
Após instalação fazer download do arquivo [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).\
O arquivo deverá ficar dentro da pasta do projeto.

### Arquivos

* **analysis-log.py** - código de acesso ao banco de e querys.
* **newsdata.sql** - arquivo de criação do banco de dados, tabelas e inserts.
* **docker-compose.yml** - arquivo de criação de imagem do postgre e adminer.
* **Pipfile e Pipfile.lock** - lista de pacotes e suas versões

### Executando o projeto
Dentro do diretório do projeto execute os seguintes comandos no terminal:
```
$ docker-compose.yml up -d
$ pipenv install
$ pipenv shell
$ python log-analysis.py
```

## Resultado
```
--------------------------------------------------+
Candidate is jerk, alleges rival - 338647views    |
Bears love berries, alleges bear - 253801views    |
Bad things gone, say good people - 170098views    |
--------------------------------------------------+
Rudolf von Treppenwitz - 338647                   |
Ursula La Multa - 253801                          |
Anonymous Contributor - 170098                    |
--------------------------------------------------+
Jul 17, 2016 - 2.26%                              |
--------------------------------------------------+
```
## Contribuindo

Depois de aprovado pela **Udacity** contribuições serão bem vindas.