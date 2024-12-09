
---

# **Documentação Completa do Projeto - Gerenciamento Financeiro**

## **Visão Geral**
Este projeto implementa um sistema de gerenciamento financeiro com autenticação de usuários e controle de transações financeiras. Ele foi desenvolvido utilizando **Django**, **Django REST Framework** (DRF), e está containerizado com **Docker**. A aplicação foi projetada para gerenciar transações financeiras associadas a um usuário específico e utiliza tokens JWT para autenticação e autorização.

---

## **Principais Funcionalidades**
- **Cadastro e autenticação de usuários**: Criação de contas de usuários e gerenciamento de login/logout com autenticação baseada em tokens JWT.
- **Registro e gerenciamento de transações financeiras**: O usuário pode criar, atualizar, listar e excluir transações financeiras, todas vinculadas ao seu perfil.
- **API protegida por autenticação**: Todos os endpoints que manipulam dados de transações financeiras são acessíveis apenas para usuários autenticados.
- **Swagger para documentação da API**: A API é documentada automaticamente utilizando o Swagger UI para facilitar a visualização e o uso dos endpoints.

---

## **Configuração e Execução**

### **Pré-requisitos**
Certifique-se de que os seguintes itens estão instalados:
- **Docker**: [Instalar Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Instalar Docker Compose](https://docs.docker.com/compose/install/)

### **Passo a Passo**

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   ```

2. **Construa e inicie os containers**:
   O **entrypoint** já foi configurado para rodar automaticamente os comandos de migração e iniciar o servidor do Django. Para isso, basta executar:
   ```bash
   docker-compose up --build
   ```

   Este comando irá:
   - Criar as imagens do Docker.
   - Executar as migrações no banco de dados.
   - Iniciar o servidor Django.

3. **Acesse o projeto**:
   - O servidor Django estará disponível em: [http://localhost:8000](http://localhost:8000).

---

## **Estrutura do Projeto**
```plaintext
.
├── authentication/       # App responsável pelo gerenciamento de usuários e autenticação
├── financial_transaction/ # App responsável pelas transações financeiras
├── docker-compose.yml    # Configuração do Docker Compose
├── Dockerfile            # Configuração do Docker para o projeto Django
├── requirements.txt      # Dependências do Python
├── manage.py             # Comando de gerenciamento do Django
└── ...
```

---

## **Comandos Úteis**

1. **Acessar o container do Django**:
   Caso precise acessar o shell do container, use:
   ```bash
   docker-compose exec web bash
   ```

2. **Criar um superusuário**:
   Caso precise criar um superusuário, execute o seguinte comando dentro do container:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

3. **Coletar arquivos estáticos**:
   Caso precise coletar os arquivos estáticos, execute:
   ```bash
   docker-compose exec web python manage.py collectstatic
   ```

4. **Parar os containers**:
   Para parar os containers, use:
   ```bash
   docker-compose down
   ```

---

## **API Endpoints**

Abaixo estão os endpoints disponíveis na API do sistema. Todos os endpoints de transações financeiras retornam dados **somente do usuário autenticado**, ou seja, cada transação financeira estará associada ao usuário logado.

### **Autenticação**
| Método | Endpoint                        | Descrição                |
|--------|---------------------------------|--------------------------|
| POST   | `/api/v1/authentication/token/` | Geração de token de acesso (login) |
| POST   | `/api/v1/authentication/refresh/token/` | Renovação do token |
| POST   | `/api/v1/authentication/register/` | Cadastro de usuário      |
| POST   | `/api/v1/authentication/verify/token/` | Verificação de token |

### **Transações Financeiras**
| Método | Endpoint                          | Descrição                                       |
|--------|-----------------------------------|-------------------------------------------------|
| GET    | `/api/v1/financial-transaction/`  | Lista todas as transações financeiras do usuário autenticado |
| POST   | `/api/v1/create-financial-transaction/` | Cria uma nova transação financeira para o usuário autenticado |
| PUT    | `/api/v1/update-delete-financial-transaction/<id>/` | Atualiza uma transação financeira do usuário autenticado |
| DELETE | `/api/v1/update-delete-financial-transaction/<id>/` | Deleta uma transação financeira do usuário autenticado |

### **Usuários**
| Método | Endpoint                          | Descrição                                       |
|--------|-----------------------------------|-------------------------------------------------|
| DELETE | `/api/v1/user/del/{id}/`          | Deleta um usuário |
| PUT    | `/api/v1/user/update/{id}/`       | Atualiza os dados de um usuário específico |
| PATCH  | `/api/v1/user/update/{id}/`       | Atualiza parcialmente os dados de um usuário específico |
| GET    | `/api/v1/users/all/`              | Lista todos os usuários |

---

## **Documentação Swagger**

A documentação da API está disponível através do Swagger UI, acessível pelo seguinte endpoint após a execução do Docker:
- [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Este endpoint fornece uma interface interativa para explorar todos os endpoints da API e testar as requisições diretamente na interface web.

---

## **Testes**

1. **Executar os testes com Docker**:
   Para rodar os testes automatizados, execute o seguinte comando:
   ```bash
   docker-compose exec web python manage.py test
   ```

2. **Estrutura de testes**:
   - Os testes estão organizados por app. Cada app possui um diretório `tests/` com seus respectivos testes.
   - São usados `APITestCase` do Django REST Framework para realizar os testes dos endpoints da API.

---

## **Considerações Finais**

- O projeto foi configurado para ser **containerizado com Docker**, facilitando o ambiente de desenvolvimento e a implantação.
- A **autenticação via tokens JWT** garante que somente usuários autenticados possam acessar e manipular suas transações financeiras.
- A documentação gerada automaticamente pelo **Swagger UI** oferece uma maneira prática de testar e entender a API.


---


