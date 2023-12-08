from mysql_connector import connection
import mysql.connector

def addPublisher(name, phone, city):
    # inserts a tuple into Publisher
    cursor = connection.cursor()
    query = "INSERT INTO Publisher VALUES ('{}', {}, {})".format(
        name,
        "'{}'".format(phone) if phone.lower() != 'null' else 'NULL',
        "'{}'".format(city) if city.lower() != 'null' else 'NULL',
)
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.close()
        return "Duplicate entry: publisher <" + name + "> already exists!"
    except mysql.connector.Error as err:
        return "Error: " + str(err)
    cursor.close()
    return "Publisher <" + name + "> added successfully"


def addBook(isbn, title, year, published_by, prev_edi, price):
    # inserts a tuple into Book
    cursor = connection.cursor()
    query = "INSERT INTO Book VALUES ('{}', {}, {}, {}, {}, {})".format(
        isbn,
        "'{}'".format(title) if title.lower() != 'null' else 'NULL',
        "'{}'".format(year) if year.lower() != 'null' else 'NULL',
        "'{}'".format(published_by) if published_by.lower() != 'null' else 'NULL',
        "'{}'".format(prev_edi) if prev_edi.lower() != 'null' else 'NULL',
        "'{}'".format(price) if price.lower() != 'null' else 'NULL'
)
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as err:
        return "Error: "+ str(err)
    cursor.close()
    return "Book <" + title + "> added successfully"
    

def editBook(isbn, title, year, published_by, prev_edi, price):
    # edit a book in the database
    cursor = connection.cursor()
    query = "UPDATE Book SET title = {}, year = {}, published_by = {}, previous_edition = {}, price = {}".format(
        "'{}'".format(title) if title.lower() != 'null' else 'NULL',
        "'{}'".format(year) if year.lower() != 'null' else 'NULL',
        "'{}'".format(published_by) if published_by.lower() != 'null' else 'NULL',
        "'{}'".format(prev_edi) if prev_edi.lower() != 'null' else 'NULL',
        "'{}'".format(price) if price.lower() != 'null' else 'NULL'  
    ) + " WHERE isbn = " + isbn  # Add the WHERE clause outside the format string
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as err:
        return "Error: "+ str(err)
    cursor.close()
    return "Book <" + isbn + "> updated successfully"


def deleteBook(isbn):
    cursor = connection.cursor()
    query = "DELETE FROM Book WHERE isbn = " + isbn
    try:
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as err:
        return "Error: " + str(err)
    cursor.close()
    return "Book <" + isbn + "> deleted successfully"


def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
    

def findByTitle(title):
    # returns all tuples in Book with specified title attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.title='" + title + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByISBN(isbn):
    # returns all tuples in Book with specified isbn attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.ISBN='" + isbn + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByPublisher(publisher):
    # returns all tuples in Book with specified publisher attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.published_by='" + publisher + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByPriceRange(low, high):
    # returns all tuples in Book with specified price range attribute
    cursor = connection.cursor()
    query = "SELECT * FROM Book WHERE price BETWEEN " + str(low) + " AND " + str(high) + ";"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByYear(year):
    # returns all tuples in Book with specified year attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.year='" + str(year) + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByTitleAndPublisher(title, publisher):
    # returns all tuples in Book with specified title and publisher attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.title='" + title + "' and Book.published_by='" + publisher + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results





