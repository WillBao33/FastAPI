from fastapi import FastAPI, Body, status

app = FastAPI()

BOOKS = [
    {'title': 'Book 1', 'author': 'Author One', 'year': "2008"},
    {'title': 'Book 2', 'author': 'Author Two', 'year': "1965"},
    {'title': 'Book 3', 'author': 'Author Three', 'year': "1996"},
    {'title': 'Book 4', 'author': 'Author Four', 'year': "2013"},
    {'title': 'Book 5', 'author': 'Author Five', 'year': "2022"},
    {'title': 'Book 6', 'author': 'Author Two', 'year': "1973"},
]
@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async  def read_year_by_query(year: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('year').casefold() == year.casefold():
            book_to_return.append(book)

    return book_to_return

@app.get("/books/{book_author}/")
async def read_author_year_by_query(author: str, year: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('year') == year.casefold():
            book_to_return.append(book)
    return book_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book
            return BOOKS[i]

@app.delete("/books/{book_title}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_title: str):
    for index, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.pop(index)
            return
    return {"error": "Book not found"}

@app.get("/books/{book_author}/)")
async def read_author_book(book_author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            book_to_return.append(book)
    return book_to_return