# Define the Book class with name, rate, price, author, and genre
class Book:
    def __init__(self, name, rate, price, author, genre):
        self.name = name
        self.rate = rate
        self.price = price
        self.author = author
        self.genre = genre
    
    def display_info(self):
        return (
            f"Book Name: {self.name}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Rate: {self.rate}/5\n"
            f"Price: ${self.price}\n"
        )

# Welcome message with LitLibrary
print("Welcome to LitLibrary\n")

# Function to create a new book
def create_book(name, author, genre, rate, price):
    return Book(name, rate, price, author, genre)

# Function to search for books by genre or author
def search_books(books, keyword):
    print(f"\nSearch results for '{keyword}' in LitLibrary:")
    found = False
    for book in books:
        if keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower():
            print(book.display_info())
            print("-" * 40)
            found = True
    if not found:
        print("No matching books found.\n")

# Function to display all books
def display_all_books(books):
    print("\nAll Available Books in LitLibrary:")
    for i, book in enumerate(books, 1):
        print(f"Book #{i}:")
        print(book.display_info())
        print("-" * 40)

# Function to find highest rated book
def find_highest_rated(books):
    if not books:
        return None
    highest_rated = max(books, key=lambda book: book.rate)
    return highest_rated

# Function to filter books by price range
def filter_by_price(books, min_price=0, max_price=float('inf')):
    filtered_books = [book for book in books if min_price <= book.price <= max_price]
    return filtered_books

# Creating initial book objects
book1 = Book("The Great Gatsby", 4.5, 10.99, "F. Scott Fitzgerald", "Classic")
book2 = Book("1984", 4.8, 8.99, "George Orwell", "Dystopian")
book3 = Book("To Kill a Mockingbird", 4.7, 12.99, "Harper Lee", "Historical Fiction")
book4 = Book("The Hobbit", 4.6, 9.99, "J.R.R. Tolkien", "Fantasy")
book5 = Book("Pride and Prejudice", 4.4, 7.99, "Jane Austen", "Romance")

# Store books in a list
books = [book1, book2, book3, book4, book5]

# Simulate adding a new book
add_more = True
if add_more:
    simulated_book = create_book("Clean Code", "Robert C. Martin", "Programming", 4.9, 29.99)
    books.append(simulated_book)
    print(f"Added new book to LitLibrary: {simulated_book.name}")

# Simulate searching for a book
search = True
if search:
    keyword = "Programming"  # You can change this keyword to test different searches
    search_books(books, keyword)

# Display all books
display_all_books(books)

# Show highest rated book
highest_rated = find_highest_rated(books)
if highest_rated:
    print(f"\nHighest Rated Book in LitLibrary:")
    print(highest_rated.display_info())
    print("-" * 40)

# Show books under $10
affordable_books = filter_by_price(books, max_price=10.00)
if affordable_books:
    print(f"\nBooks under $10 in LitLibrary:")
    for book in affordable_books:
        print(f"- {book.name}: ${book.price}")
    print()

print(f"\nTotal books in LitLibrary: {len(books)}")