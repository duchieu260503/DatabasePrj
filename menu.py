import sys
import book_dao
import validate
import search_functions

# Define menu options for the main menu
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit'
}

# Define sub-menu options for book search functionality
search_menu_options = {
    1: 'Search all books',
    2: 'Search with title',
    3: 'Search with ISBN',
    4: 'Search with publisher',
    5: 'Search with price range',
    6: 'Search with year',
    7: 'Search with title and publisher',
    8: 'Return to normal menu'
}


def option1():  # add a publisher
    print("-------Add Publisher-------")
    print("Type NULL for no entry.")
    name = validate.publisher_constraints()
    phone = str(validate.ten_number_constraints("Phone number"))
    city = str(validate.city_constraint())
    result = book_dao.addPublisher(name, phone, city)
    print(result)


def option2(): # add a book
    print("-------Add Book-------")
    print("Type NULL for no entry.")
    isbn = str(validate.ten_number_constraints("ISBN"))
    title = validate.book_title_constraints()
    year = str(validate.get_year_input())
    published_by = validate.publisher_constraints()
    previous_edition = str(validate.ten_number_constraints("Previous Edition"))
    price = str(validate.price_constraints(""))
    result = book_dao.addBook(isbn, title, year, published_by, previous_edition, price)
    print(result)


def option3(): # edit a book
    print("-------Edit Book-------")
    print("Type NULL for no entry.")
    isbn = str(validate.ten_number_constraints("ISBN"))
    title = validate.book_title_constraints()
    year = str(validate.get_year_input())
    published_by = validate.publisher_constraints()
    previous_edition = str(validate.ten_number_constraints("Previous Edition"))
    price = str(validate.price_constraints(""))
    result = book_dao.editBook(isbn, title, year, published_by, previous_edition, price)
    print(result)


def option4(): # delete a book
    print("-------Delete Book-------")
    isbn = str(validate.ten_number_constraints("ISBN"))
    result = book_dao.deleteBook(isbn)
    print(result)


def option5(): # search books
    # A sub-menu shall be printed and prompt user selection
    print("---------------Book Search Function---------------\n")

    option = ''
    while(option != 8):
        # user selection of options and actions
        try:
            # print_search_menu
            for key in search_menu_options.keys():
                print (str(key)+'.', search_menu_options[key], end = "\n")
            option = int(input("\n\nPlease select an option, type [1 - 8] and press enter:\n"))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1: #Search all books
            print("Search Option 1: all books were chosen")
            search_functions.search_all_books()
        elif option == 2: #Search with title
            print("Search Option 2: Search with title")
            title = validate.book_title_constraints()
            search_functions.search_by_title(title)
        elif option == 3: #Search with ISBN
            print("Search Option 3: Search with ISBN")
            isbn = validate.ten_number_constraints("ISBN")
            search_functions.search_by_isbn(isbn)
        elif option == 4: #Search with publisher
            print("Search Option 4: Search with publisher")
            publisher = validate.publisher_constraints()
            search_functions.search_by_publisher(publisher)
        elif option == 5: #Search with price range
            print("Search Option 5: Search with price range")
            low = validate.price_constraints(" lower bound")
            high = validate.price_constraints(" higher bound")
            search_functions.search_by_price_range(low, high)
        elif option == 6: #Search with year
            print("Search Option 6: Search with year")
            year = validate.get_year_input()
            search_functions.search_by_year(year)
        elif option == 7: #Search with title and publisher
            print("Search Option 7: Search with title and publisher")
            title = validate.book_title_constraints()
            publisher = validate.publisher_constraints()
            search_functions.search_by_title_and_publisher(title, publisher)
        elif option == 8: # Exit the loop, return to normal program
            pass
        else:
            print('Invalid option. Please enter a number between 1 and 8.')


# Main function to run the program
if __name__ == '__main__':
    # Main loop for the program
    while True:
        print("--------------------------------------------Book Manager Software-------------------------------------------\n")
        # Print main menu options
        for key in menu_options.keys():
            print (str(key) + '.', menu_options[key], end="  ")
        option = ''
        try:
            option = int(input("\n\nPlease select a function, type [1 - 6] and press enter:\n"))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check user choice and execute corresponding function
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks for using our database services! Goodbye.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')










