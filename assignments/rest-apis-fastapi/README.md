# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Você vai construir uma API REST completa para um catálogo de livros usando o framework FastAPI. Ao final, você saberá criar rotas, validar dados com Pydantic e implementar as operações CRUD (criar, ler, atualizar e remover).

## 📝 Tasks

### 🛠️ Primeira API e Rotas de Leitura

#### Descrição
Crie uma aplicação FastAPI e implemente as rotas que apenas leem informações do catálogo de livros. Use a lista `books` já disponível no starter code como "banco de dados" em memória.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI()` chamada `app`
- Responder em `GET /` com a mensagem `{"message": "Book Catalog API"}`
- Responder em `GET /books` com a lista completa de livros
- Responder em `GET /books/{book_id}` com um único livro, buscado pelo seu `id`
- Rodar com `uvicorn main:app --reload` e exibir a documentação automática em `http://127.0.0.1:8000/docs`

Exemplo de resposta para `GET /books/1`:

```json
{
  "id": 1,
  "title": "O Hobbit",
  "author": "J.R.R. Tolkien",
  "year": 1937
}
```

### 🛠️ Validação de Dados com Pydantic

#### Descrição
Defina um modelo Pydantic para descrever um livro e use-o para validar automaticamente os dados que chegam na sua API.

#### Requisitos
O programa completo deve:

- Definir uma classe `Book` que herda de `BaseModel` com os campos `title` (str), `author` (str) e `year` (int)
- Usar o modelo `Book` como tipo do parâmetro do corpo da requisição
- Responder em `POST /books` criando um novo livro e retornando-o com um `id` gerado automaticamente
- Retornar o status code `201` ao criar um livro com sucesso
- Rejeitar automaticamente requisições com campos faltando ou com tipo errado (o FastAPI faz isso por você — teste enviando um `year` como texto)

Exemplo de corpo enviado em `POST /books`:

```json
{
  "title": "Dom Casmurro",
  "author": "Machado de Assis",
  "year": 1899
}
```

### 🛠️ CRUD Completo e Tratamento de Erros

#### Descrição
Finalize a API implementando as rotas de atualização e remoção, e trate os casos em que o livro solicitado não existe.

#### Requisitos
O programa completo deve:

- Responder em `PUT /books/{book_id}` atualizando os dados de um livro existente e retornando o livro atualizado
- Responder em `DELETE /books/{book_id}` removendo o livro e retornando o status code `204`
- Levantar `HTTPException` com status `404` e a mensagem `"Book not found"` quando o `book_id` não existir (em `GET`, `PUT` e `DELETE`)
- Adicionar uma rota `GET /books/search/?author=<nome>` que retorna apenas os livros do autor informado usando query parameter
- Retornar uma lista vazia (e não um erro) quando a busca não encontrar nenhum livro
