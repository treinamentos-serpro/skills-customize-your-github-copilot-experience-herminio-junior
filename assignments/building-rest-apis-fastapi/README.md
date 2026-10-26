# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to manage tasks, practicing HTTP methods, request and response data, and status codes. The API will store data in memory, so no database is required.

## 📝 Tasks

### 🛠️ Listar e criar tarefas

#### Descrição
Complete os endpoints para consultar a lista de tarefas e adicionar uma nova tarefa. Para executar o projeto, instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`. A documentação interativa ficará disponível em `/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para retornar todas as tarefas
- Implementar `POST /tasks` para criar uma tarefa com título e estado inicial `completed` igual a `false`
- Atribuir um ID único à tarefa criada e retornar a tarefa na resposta
- Responder à criação com o status HTTP `201 Created`

### 🛠️ Consultar uma tarefa pelo ID

#### Descrição
Adicione um endpoint para buscar uma tarefa específica usando seu ID, mantendo o mesmo formato de dados usado na lista.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}`
- Retornar a tarefa quando o ID existir
- Retornar o status HTTP `404 Not Found` quando o ID não existir

### 🛠️ Atualizar e remover tarefas

#### Descrição
Permita alterar os dados de uma tarefa existente e removê-la da lista em memória.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar o título, o estado `completed` ou ambos
- Manter sem alteração os campos que não forem enviados na atualização
- Implementar `DELETE /tasks/{task_id}` e responder com o status HTTP `204 No Content` quando a remoção for concluída
- Retornar `404 Not Found` ao tentar atualizar ou remover uma tarefa inexistente
