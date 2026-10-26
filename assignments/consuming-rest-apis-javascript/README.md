# 📘 Assignment: Consuming REST APIs with JavaScript

## 🎯 Objective

Build a browser interface that communicates with the Task API created in **Building REST APIs with FastAPI**. Practice asynchronous JavaScript, JSON, HTTP methods, and handling API responses.

## 📝 Tasks

### 🛠️ Carregar e exibir tarefas

#### Descrição
Crie `index.html` e `app.js` para buscar as tarefas da API e apresentá-las em uma página web. Inicie a API com `uvicorn starter-code:app --reload` no diretório da atividade FastAPI e sirva a interface com `python -m http.server 5500` no diretório dos arquivos web. A API estará em `http://127.0.0.1:8000` e a interface em `http://localhost:5500`.

#### Requisitos
A interface concluída deve:

- Usar `fetch()` para enviar `GET /tasks`
- Exibir o título e o estado de conclusão de cada tarefa retornada
- Mostrar estados visíveis de carregamento, lista vazia e erro de conexão
- Permitir que a API aceite requisições da origem `http://localhost:5500` usando CORS

### 🛠️ Criar tarefas pela interface

#### Descrição
Adicione um formulário para que o usuário cadastre novas tarefas sem acessar diretamente a documentação da API.

#### Requisitos
A interface concluída deve:

- Solicitar um título e impedir o envio quando ele estiver vazio
- Enviar `POST /tasks` com um corpo JSON no formato `{"title": "Ler um livro"}`
- Incluir o cabeçalho `Content-Type: application/json`
- Adicionar à lista a tarefa retornada quando a API responder com sucesso
- Exibir uma mensagem de erro se a criação falhar

### 🛠️ Atualizar e remover tarefas

#### Descrição
Adicione controles para marcar tarefas como concluídas ou pendentes e para removê-las da lista.

#### Requisitos
A interface concluída deve:

- Enviar `PATCH /tasks/{task_id}` com o campo `completed` atualizado
- Enviar `DELETE /tasks/{task_id}` para remover uma tarefa
- Atualizar a interface somente depois de uma resposta de sucesso da API
- Manter a tarefa na lista e informar o usuário quando uma atualização ou remoção falhar
