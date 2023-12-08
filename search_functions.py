import book_dao

# Function to print search results neatly formatted
def print_search_query(results):
    print('\n')
    s_format = "%-10s %-1s %-50s"
    if len(results) == 0:
        print("No matches found.")
    else:
        print(s_format % ("ISBN:", "|", "Title:"))
        for item in results:
            print(s_format % (item[0], "|", item[1]))
    print("---End of Search Results---\n\n")

def search_all_books():
    # Use a data access object (DAO) to abstract the retrieval of data from  a data resource such as a database.
    results = book_dao.findAll()
    # Display results
    print_search_query(results)
    

def search_by_title(title):
    results = book_dao.findByTitle(title)
    print_search_query(results)


def search_by_isbn(isbn):
    results = book_dao.findByISBN(isbn)
    print_search_query(results)


def search_by_publisher(publisher):
    results = book_dao.findByPublisher(publisher)
    print_search_query(results)


def search_by_price_range(low, high):
    results = book_dao.findByPriceRange(low, high)
    print_search_query(results)


def search_by_year(year):
    results = book_dao.findByYear(year)
    print_search_query(results)


def search_by_title_and_publisher(title, publisher):
    results = book_dao.findByTitleAndPublisher(title, publisher)
    print_search_query(results)