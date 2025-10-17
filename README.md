# LitLibrary 📚

A simple, command-line-based Python application for managing a collection of books. This project demonstrates basic Object-Oriented Programming (OOP) principles by defining a `Book` class and functions to interact with a list of book objects.

## Features

-   **Object-Oriented Design**: Uses a `Book` class to neatly structure data for each book.
-   **Add Books**: A function to create and add new books to the library.
-   **Display All Books**: View a formatted list of all books currently in the library.
-   **Search Functionality**: Search for books by `author` or `genre`.
-   **Find Highest Rated**: Automatically identifies and displays the book with the highest rating.
-   **Filter by Price**: Lists all books that fall within a specified price range (e.g., under $10).

## Getting Started

To run this project on your local machine, follow these simple steps.

### Prerequisites

Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Harsh151999/LitLibrary.git](https://github.com/Harsh151999/LitLibrary.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd LitLibrary
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```
    The script will run and print the output directly to the console. You can modify the script (`main.py`) to change the search keywords or add different books.

## Code Overview

-   **`Book` class**: The core of the application. Each book is an instance of this class with the following attributes:
    -   `name`
    -   `rate`
    -   `price`
    -   `author`
    -   `genre`

-   **Main Functions**:
    -   `create_book()`: Creates a new `Book` object.
    -   `search_books()`: Iterates through the book list to find matches based on a keyword.
    -   `display_all_books()`: Prints the details of every book in the library.
    -   `find_highest_rated()`: Uses a `max()` function with a lambda key to find the book with the highest `rate`.
    -   `filter_by_price()`: Uses a list comprehension to return books within a price range.

## Future Improvements

This is a simple simulation. Here are some ideas for how it could be expanded:

-   [ ] Implement an interactive Command Line Interface (CLI) for users.
-   [ ] Save the book library to a file (e.g., CSV or JSON) to persist data between sessions.
-   [ ] Add functionality to remove or edit existing books.
-   [ ] Expand search and filtering capabilities (e.g., search by name, filter by rating).
