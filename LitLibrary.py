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
            f"Rating: {self.rate}/5\n"
            f"Price: ${self.price:.2f}\n"
        )
    
    def __str__(self):
        return self.display_info()
    
    def __repr__(self):
        return f"Book('{self.name}', {self.rate}, {self.price}, '{self.author}', '{self.genre}')"

class LitLibrary:
    def __init__(self, name="LitLibrary"):
        self.name = name
        self.books = []
        self._initialize_sample_books()
    
    def _initialize_sample_books(self):
        """Initialize with sample books"""
        sample_books = [
            Book("The Great Gatsby", 4.5, 10.99, "F. Scott Fitzgerald", "Classic"),
            Book("1984", 4.8, 8.99, "George Orwell", "Dystopian"),
            Book("To Kill a Mockingbird", 4.7, 12.99, "Harper Lee", "Historical Fiction"),
            Book("The Hobbit", 4.6, 9.99, "J.R.R. Tolkien", "Fantasy"),
            Book("Pride and Prejudice", 4.4, 7.99, "Jane Austen", "Romance")
        ]
        self.books.extend(sample_books)
    
    def add_book(self, name, author, genre, rate, price):
        """Add a new book to the library"""
        new_book = Book(name, rate, price, author, genre)
        self.books.append(new_book)
        print(f"✓ Added '{name}' to {self.name}")
        return new_book
    
    def search_books(self, keyword):
        """Search books by title, author, or genre"""
        print(f"\n🔍 Search results for '{keyword}':")
        found_books = []
        
        for book in self.books:
            if (keyword.lower() in book.name.lower() or 
                keyword.lower() in book.author.lower() or 
                keyword.lower() in book.genre.lower()):
                found_books.append(book)
        
        if found_books:
            self._display_books_list(found_books)
        else:
            print("No matching books found.")
        
        return found_books
    
    def display_all_books(self):
        """Display all books in the library"""
        print(f"\n📚 All Books in {self.name} ({len(self.books)} books):")
        self._display_books_list(self.books)
    
    def _display_books_list(self, books_list):
        """Helper method to display a list of books"""
        for i, book in enumerate(books_list, 1):
            print(f"Book #{i}:")
            print(book.display_info())
            print("-" * 40)
    
    def find_highest_rated(self):
        """Find the highest rated book(s)"""
        if not self.books:
            return None
        
        max_rating = max(book.rate for book in self.books)
        highest_rated = [book for book in self.books if book.rate == max_rating]
        
        print(f"\n⭐ Highest Rated Book(s) ({max_rating}/5):")
        self._display_books_list(highest_rated)
        return highest_rated
    
    def filter_by_price(self, min_price=0, max_price=float('inf')):
        """Filter books by price range"""
        filtered_books = [
            book for book in self.books 
            if min_price <= book.price <= max_price
        ]
        
        price_range = f"${min_price:.2f}-${max_price:.2f}" if max_price != float('inf') else f"${min_price:.2f}+"
        print(f"\n💰 Books in price range {price_range}:")
        
        if filtered_books:
            self._display_books_list(filtered_books)
        else:
            print("No books found in this price range.")
        
        return filtered_books
    
    def get_library_stats(self):
        """Get library statistics"""
        total_books = len(self.books)
        total_value = sum(book.price for book in self.books)
        avg_rating = sum(book.rate for book in self.books) / total_books if total_books > 0 else 0
        
        print(f"\n📊 {self.name} Statistics:")
        print(f"Total books: {total_books}")
        print(f"Total collection value: ${total_value:.2f}")
        print(f"Average rating: {avg_rating:.2f}/5")
        
        # Genre distribution
        genres = {}
        for book in self.books:
            genres[book.genre] = genres.get(book.genre, 0) + 1
        
        print("Genre distribution:")
        for genre, count in genres.items():
            print(f"  {genre}: {count} book(s)")
        
        return {
            'total_books': total_books,
            'total_value': total_value,
            'avg_rating': avg_rating,
            'genres': genres
        }

def main():
    """Main function to demonstrate the library system"""
    # Create library instance
    library = LitLibrary()
    
    print("=" * 50)
    print(f"Welcome to {library.name}!")
    print("=" * 50)
    
    # Add a new programming book
    library.add_book("Clean Code", "Robert C. Martin", "Programming", 4.9, 29.99)
    
    # Demonstrate searches
    library.search_books("Programming")
    library.search_books("Orwell")
    
    # Display all books
    library.display_all_books()
    
    # Show highest rated
    library.find_highest_rated()
    
    # Filter by price
    library.filter_by_price(max_price=10.00)
    
    # Show statistics
    library.get_library_stats()

if __name__ == "__main__":
    main()
