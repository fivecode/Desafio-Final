#  Code-Girls-Luiza-Code
 Projeto criado para o desenvolvimento do Desafio Final da 4ª Edição do Luiza Code - GCP

###  Desevolvido por:
- [ Carla Santos ] (https://github.com/CarlaCdosSantos)
- [ Claudia Ribeiro] (https://github.com/clauribeiro21)
- [ Erica Bernandes] (https://github.com/ericabernardess)
- [ Mariana Galdino] (https://github.com/MarianaGaldino)
- [ Tais Santos] (https://github.com/Tais-AS)

###  Proposta:
Este é um repositório referente ao desafio final do curso do Luiza Code - 4º Edição sobre GCP com parceria com a Gama Academy.
A proposta desse projeto é  para demonstrar os nossos conhecimentos adquiridos durante o curso.


###  O que deve ser feito:

O objetivo é desenvolver um sistema web de adição, atualização, filtro e remoção de produtos de determinada empresa. 
Esse serviço deve atender os seguintes requisitos:

###  ✅ Requisitos Obrigatórios:

- Deploy da aplicação em Kubernetes

- API contendo os seguintes endpoints:
    ● Listar produtos
    ● Listar empresas
    ● Cadastrar produto e empresa
    ● Adicionar um produto na lista da empresa;
    ● Remover um produto da lista da empresa; 

###  ✅ Requisitos não-obrigatórios

- Performance (Volume de milhões de transações por dia)
- Testes automatizados, integração e unitários.
- Logs / Rastreabilidade
- Tratamento de Exceção
- Front-end da aplicação


##  Instruções para configurar o ambiente e rodar o projeto:

###  Antes de começar:

1. Crie um fork do projeto:
     - Crie um fork desse projeto e para isso siga esse [ tutorial de como realizar um fork ] (https://docs.github.com/pt/github/getting-started-with-github/quickstart/fork-a-repo) ;
     - Após feito o garfo, clone o repositório criado para o seu computador.

2. Instale como dependências:
     - Nenhum terminal executa o seguinte comando:

              npm install ou npm i

3. Crie um arquivo .env:
    - Crie um arquivo .env na raiz do projeto com as seguintes seguimentos:

          # INFORMAÇÕES BANCO DE DADOS
          

          # INFORMAÇÕES USUARIO --- Altere aqui para suas informações 
          

4. Criando o banco de dados:
     - verifique se sua instácia do MySql está ativa;
     - Nenhum terminal executa o seguinte comando para criar o banco de dados:

           npx sequelize db: create

     - Nenhum terminal execute o seguinte comando para criar tabelas no banco de dados:

           npx sequelize db: migrate 

     - Nenhum terminal execute o seguinte comando para popular como tabelas com as informações necessárias:

           npx sequelize db: seed: all

5. Iniciando a aplicação:
     - Nenhum terminal executa o seguinte comando:

            npm start ou npm run dev

##  Orientadores 

* Profª [Marianne Salomão](https://github.com/mariannesalomao)
* [Gama Academy](https://www.gama.academy/)
* [Luiza Code](https://corp.gama.academy/luiza-code/inscricao)