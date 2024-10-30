from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.books_data import books
from src.books.schemas import Book, BookUpdate

book_router  = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_all_books() -> list:
  return books

@book_router.get('/{id}')
async def get_specific_book(id: int) -> dict:
  for book in books:
    if book['id'] == id:
      return book
  raise HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail="Book not found"
  )

@book_router.post('/', status_code = status.HTTP_201_CREATED)
async def create_a_book(data: Book) -> dict:
  new_book = data.model_dump()
  books.append(new_book)
  return new_book

@book_router.patch('/{id}')
async def patch_book(id: int, data: BookUpdate) -> dict:
  for book in books:
    if book['id'] == id:
      book['title'] = data.title
      book['author'] = data.author
      book['publisher'] = data.publisher
      book['page_count'] = data.page_count
      book['language'] = data.language
      return book
  raise HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail="Book not found"
  )

@book_router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
  for book in books:
    if book['id'] == id:
      books.remove(book)
      return {}
  raise HTTPException(
    status_code = status.HTTP_404_NOT_FOUND,
    detail="Book not found"
  )