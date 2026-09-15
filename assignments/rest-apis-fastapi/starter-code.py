# Código Inicial: Building REST APIs with FastAPI
#
# Instale as dependências:  pip install -r requirements.txt
# Rode o servidor:          uvicorn main:app --reload
# Documentação automática:  http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# "Banco de dados" em memória
books = [
    {"id": 1, "title": "O Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 3, "title": "O Senhor dos Anéis", "author": "J.R.R. Tolkien", "year": 1954},
]


# Tarefa 2: defina aqui o modelo Book com title, author e year
class Book(BaseModel):
    pass


@app.get("/")
def read_root():
    return {"message": "Book Catalog API"}


# Tarefa 1: retorne a lista completa de livros
@app.get("/books")
def list_books():
    pass


# Tarefa 1: retorne um único livro pelo id
# Tarefa 3: levante HTTPException(status_code=404, detail="Book not found") se não existir
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


# Tarefa 2: crie um novo livro e retorne-o com status 201
@app.post("/books", status_code=201)
def create_book(book: Book):
    pass


# Tarefa 3: atualize um livro existente
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    pass


# Tarefa 3: remova um livro e retorne status 204
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    pass


# Tarefa 3: filtre os livros pelo query parameter "author"
@app.get("/books/search/")
def search_books(author: str):
    pass
