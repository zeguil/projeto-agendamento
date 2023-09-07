

# Projeto de Agendamento de Laboratório

Este é um projeto de uma API em Django para agendamento de laboratório. Ele permite que professores e alunos façam reservas de laboratórios e gera códigos de boleto fictícios para os alunos.

## Requisitos

- Python 3.x
- Django 3.x
- Django Rest Framework

## Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone https://github.com/zeguil/projeto-agendamento.git 

2.  Crie um ambiente virtual (recomendado):
    
  
    
    `python -m venv venv` 
    
3.  Ative o ambiente virtual:
    
    Para Windows:
    
   
    
    `venv\Scripts\activate` 
    
    Para macOS e Linux:
    

    
    `source venv/bin/activate` 
    
4.  Instale as dependências:
   
    
    `pip install -r requirements.txt` 
    
5.  Configure o banco de dados:
    
	    python manage.py makemigrations	
		python manage.py migrate
    
6.  Crie um superusuário para acessar o painel de administração:
    
    
    `python manage.py createsuperuser` 
    
7.  Inicie o servidor de desenvolvimento:
    

    
    `python manage.py runserver` 
    

Acesse o painel de administração em `http://localhost:8000/admin/` e faça login com as credenciais do superusuário que você criou.

## Funcionalidades

-   **Registro de Alunos e Professores**: Crie contas para alunos e professores com informações como nome, CPF, email e telefone.
    
-   **Reserva de Laboratórios**: Alunos podem fazer reservas de laboratórios com informações de data e laboratório desejado.
    
-   **Geração de Código de Boleto**: Quando um aluno faz uma reserva, o sistema gera automaticamente um código de boleto fictício para ele.
    

## Endpoints da API

-   `/api/alunos/`: Lista de alunos registrados.
-   `/api/professores/`: Lista de professores registrados.
-   `/api/reservas/`: Lista de reservas de laboratório. (Método POST cria uma reserva com código de boleto gerado automaticamente)

