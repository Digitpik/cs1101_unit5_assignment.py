# Question 1: Managing Available Books in the Library

# Step 1: Initialize the list of available book titles
available_books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Initial list of books:", available_books)

# Step 2: Add two more books using append()
available_books.append("To Kill a Mockingbird")
available_books.append("The Great Gatsby")
print("\nAfter adding two books:", available_books)

# Step 3: Remove one damaged book using remove()
available_books.remove("Moby Dick")
print("\nAfter removing damaged book ('Moby Dick'):", available_books)

# Step 4: Sort the list alphabetically and display the final list
available_books.sort()
print("\nFinal sorted book list:", available_books)

# Question 2: Borrower's Immutable Details Handling

# Step 1: Create a tuple representing borrower personal details
borrower_info = ("John Doe", "B1023", "2025-10-15")
print("Borrower Info Tuple:", borrower_info)

# Step 2: Attempting to modify an element (Demonstrating Immutability)
try:
    borrower_info[1] = "B9999"
except TypeError as e:
    print("\nModification Error Observed:", e)

# Discussion of Observation:
# The TypeError confirms that tuples are immutable in Python. 
# Attempting to assign a new value to an index raises an exception,
# ensuring the borrower's record remains secure and unaltered.

# Step 3: Print the length of the tuple and iterate through its elements
print("\nTotal data fields in record:", len(borrower_info))
print("\nDisplaying record fields via loop:")
for field in borrower_info:
    print("-", field)

    # Question 3: Tuple Packing and Unpacking

# Step 1: Pack book details into a single tuple
book_info = ("The Alchemist", "Paulo Coelho", 1988)

# Step 2: Unpack the tuple into separate variables
title, author, year = book_info

# Step 3: Display unpacked data in a formatted layout
print("--- Book Information Record ---")
print(f"Title: {title}")
print(f"Author: {author}")
print(f"Publication Year: {year}")

# Question 4: Indexing and Slicing Weekly Statistics

# Given dataset: 7 weeks of borrowing statistics
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original Borrowing Statistics:", borrowed_books)

# Step 1: Extract records from Week 2 to Week 5 using slicing [index 1 to 5]
week_2_to_5 = borrowed_books[1:5]

# Step 2: Replace Week 1 value (index 0) with 20 using indexing
borrowed_books[0] = 20

# Step 3: Display updated list and extracted sub-slice
print("\nUpdated Borrowing Statistics (Week 1 corrected):", borrowed_books)
print("Extracted Statistics (Week 2 to Week 5):", week_2_to_5)