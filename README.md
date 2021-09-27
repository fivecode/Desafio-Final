#  Five-Code-Luiza-Code
 Projeto criado para o desenvolvimento do Desafio Final da 3ª Edição do Luiza Code - GCP

## Desevolvido por:
- [ Carla Santos ] (https://github.com/CarlaCdosSantos)
- [ Claudia Ribeiro] (https://github.com/clauribeiro21)
- [ Erica Bernandes] (https://github.com/ericabernardess)
- [ Mariana Galdino] (https://github.com/MarianaGaldino)
- [ Tais Santos] (https://github.com/Tais-AS)

##  Proposta:
Este é um repositório referente ao desafio final do curso do Luiza Code - 3º Edição sobre GCP com parceria com a Gama Academy.
A proposta desse projeto é  para demonstrar os nossos conhecimentos adquiridos durante o curso.

##  O que deve ser feito:
O objetivo é Desenvolver um sistema web com as funcionalidades de listar, cadastrar, adicionar e remover produtos de um marketplace de uma empresa de cosméticos.
Esse serviço deve atender os seguintes requisitos:

### :marca_de_verificação_branca: Requisitos Obrigatórios:
- Deploy da aplicação em Kubernetes
- API contendo os seguintes endpoints:
  ● Listar produtos
  ● Listar empresas
  ● Cadastrar produto e empresa
  ● Adicionar um produto na lista da empresa;
  ● Remover um produto da lista da empresa; 

###  :marca_de_verificação_branca: Requisitos não-obrigatórios:
- Performance (Volume de milhões de transações por dia)
- Testes automatizados, integração e unitários.
- Logs / Rastreabilidade
- Tratamento de Exceção
- Front-end da aplicação

### :marca_de_verificação_branca: Tecnologias utilizadas
O projeto foi criado usando as tecnologias:
- GitHub
- Python
- Docker
- Django
- JavaScript
- SQLite
- VsCode
- Meet
- Zoom
- Slack
- Plataforma Gama
- Youtube

##  Instruções para configurar o ambiente e rodar o projeto:

###  Antes de começar:
1. Clonar o respositório
Comece clonando esse projeto para a sua máquina local.
git clone https://github.com/fivecode/Desafio-Final.git
2. Instale como dependências:
     - Nenhum terminal executa o seguinte comando:
              npm install ou npm i
3. Configurando DOCKER num projeto DJANGO
>Subiu arquivos da aplicação para VSCODE
> Primeiro crie o arquivo Dockerfile
FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
> Depois build a imagem seguindo esse formato de tag:
    docker build -t mfivecode .
> Depois rode a imagem
    docker run -d -p 8000:8000 fivecode
> Agora no terminal logue no DockerHub
    dock

4. Kubernets

Criação do  deployemnt/para encapsular pods
>kubectl apply -f fivecode-deployment.yaml

Cria os pods
>kubectl get pods

Liga  cluster e mostra via web/interface 
>kubectl apply -f fivecode-service.yaml

Mostrar o service que esta atrelado ao pods
>kubectl get service
 kubectl apply -f fivecode-deployment.yaml

##  Orientadores 
* Profª [Marianne Salomão](https://github.com/mariannesalomao)
* [Gama Academy](https://www.gama.academy/)
* [Luiza Code](https://corp.gama.academy/luiza-code/inscricao)