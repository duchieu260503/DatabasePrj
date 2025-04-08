# 📚 Book Manager System

A simple MySQL-based system to manage books and publishers via Python.

## ✅ Features

- Add, edit, delete books and publishers
- Search books by:
  - ISBN
  - Title
  - Publisher
  - Year
  - Price range
  - Title + Publisher

## 🛠️ Functions Overview

### `addPublisher(name, phone, city)`
Insert a new publisher.

### `addBook(isbn, title, year, published_by, prev_edi, price)`
Insert a new book.

### `editBook(isbn, title, year, published_by, prev_edi, price)`
Update book details by ISBN.

### `deleteBook(isbn)`
Delete a book by ISBN.

### Search Functions
- `findAll()`
- `findByTitle(title)`
- `findByISBN(isbn)`
- `findByPublisher(publisher)`
- `findByPriceRange(low, high)`
- `findByYear(year)`
- `findByTitleAndPublisher(title, publisher)`

## 📦 Requirements

- Python 3.x
- `mysql-connector-python`

Install dependencies:
```
pip install mysql-connector-python
```
## 🔌 Setup
1. Configure your DB connection in mysql_connector.py.

2. Use the functions to interact with your Book and Publisher tables.
---
## License
MIT License © Hieu Pham

