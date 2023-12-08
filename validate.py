# Function to handle price input with optional 'NULL' value
def price_constraints(prompt):
    while True:
        try:
            price_input = input("Enter price" + prompt + ": ")
            if str(price_input).upper() == 'NULL':
                return price_input
            price = float(price_input)  # Convert input to a floating-point number
            return price
        except ValueError:
            print("Error: Invalid price. Please enter a valid number.")  # Handle invalid input with a message

# Function to validate and retrieve a 10-digit number input with optional 'NULL' value
def ten_number_constraints(prompt):
    variable = input("Enter " + prompt + ": ")
    if str(variable).upper() == 'NULL':
        return variable
    while len(variable) != 10 or not variable.isdigit():
        print("Error: " + prompt + " must be a 10-digit number!")  # Validate input length and digits
        variable = input("Enter " + prompt + ": ")
    return variable

# Function to validate and retrieve a published year within the range of 1900 to the current year
def get_year_input():
    while True:
        try:
            user_input = input("Enter published year: ")
            if str(user_input).upper() == 'NULL':
                return user_input
            user_input = int(user_input)  # Convert input to an integer
            current_year = 2023
            if 1900 <= user_input <= current_year:  # Validate input within the specified range
                return user_input
            else:
                print("Error: Please enter a year between 1900 and", current_year)  # Provide error message for out-of-range input
        except ValueError:
            print("Error: Invalid input. Please enter a valid year.")  # Handle non-integer input with a message

# Function to validate and retrieve a publisher name with a maximum length of 25 characters
def publisher_constraints():
    publisher = input("Enter publisher name: ")
    while publisher == "" or len(publisher) > 25:
        if publisher == "":
            print("Error: Publisher name cannot be empty!")  # Handle empty input with an error message
        else:
            print("Error: Publisher name too long (max 25 characters)!")  # Handle excessive length with an error message
        publisher = input("Enter publisher name: ")
    return publisher

# Function to validate and retrieve a book title with a maximum length of 50 characters
def book_title_constraints():
    title = input("Enter book title: ")
    while title == "" or len(title) > 50:
        if title == "":
            print("Error: Book title cannot be empty!")  # Handle empty input with an error message
        else:
            print("Error: Book title too long (max 50 characters)!")  # Handle excessive length with an error message
        title = input("Enter book title: ")
    return title

# Function to validate and retrieve a city name with a maximum length of 20 characters
def city_constraint():
    city = input("Enter City: ")
    while city == "" or len(city) > 20:
        if city == "":
            print("Error: City name cannot be empty!")  # Handle empty input with an error message
        else:
            print("Error: City name too long (max 20 characters)!")  # Handle excessive length with an error message
        city = input("Enter City: ")
    return city
