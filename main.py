import os

BOOKS_FILE = "books.txt"
MEMBERS_FILE = "members.txt"
LOANS_FILE = "loans.txt"

# ---------- Utility Functions ----------

def load_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_file(filename, data):
    with open(filename, "w") as f:
        for line in data:
            f.write(line + "\n")

# ---------- Display Functions ----------

def view_books():
    books = load_file(BOOKS_FILE)
    print("\n--- Book List ---")
    for book in books:
        book_id, title, author, status = book.split(",")
        print(f"{book_id}. {title} by {author} [{status}]")

def view_members():
    members = load_file(MEMBERS_FILE)
    print("\n--- Members ---")
    for member in members:
        member_id, name = member.split(",")
        print(f"{member_id}. {name}")

def view_loans():
    loans = load_file(LOANS_FILE)
    print("\n--- Active Loans ---")
    if not loans:
        print("No active loans.")
    for loan in loans:
        book_id, member_id = loan.split(",")
        print(f"Book ID {book_id} loaned to Member ID {member_id}")

# ---------- Core Features ----------

def loan_book():
    books = load_file(BOOKS_FILE)
    loans = load_file(LOANS_FILE)

    view_books()
    book_id = input("Enter Book ID to loan: ")
    member_id = input("Enter Member ID: ")

    updated_books = []
    found = False

    for book in books:
        b_id, title, author, status = book.split(",")

        if b_id == book_id:
            if status == "Loaned":
                print("Book already loaned.")
                return
            updated_books.append(f"{b_id},{title},{author},Loaned")
            loans.append(f"{book_id},{member_id}")
            found = True
        else:
            updated_books.append(book)

    if not found:
        print("Invalid Book ID.")
        return

    save_file(BOOKS_FILE, updated_books)
    save_file(LOANS_FILE, loans)

    print("Book loaned successfully.")

def return_book():
    books = load_file(BOOKS_FILE)
    loans = load_file(LOANS_FILE)

    book_id = input("Enter Book ID to return: ")

    updated_books = []
    updated_loans = []

    for book in books:
        b_id, title, author, status = book.split(",")
        if b_id == book_id:
            updated_books.append(f"{b_id},{title},{author},Available")
        else:
            updated_books.append(book)

    for loan in loans:
        l_book_id, member_id = loan.split(",")
        if l_book_id != book_id:
            updated_loans.append(loan)

    save_file(BOOKS_FILE, updated_books)
    save_file(LOANS_FILE, updated_loans)

    print("Book returned successfully.")

# ---------- Menu ----------

def menu():
    while True:
        print("\n--- Library System ---")
        print("1. View Books")
        print("2. View Members")
        print("3. View Loans")
        print("4. Loan Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            view_members()
        elif choice == "3":
            view_loans()
        elif choice == "4":
            loan_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
