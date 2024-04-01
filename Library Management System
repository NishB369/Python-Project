from datetime import datetime, timedelta

catalog={
    1: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'quantity': 5},
    2: {'title': '1984', 'author': 'George Orwell', 'quantity': 3},
    3: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'quantity': 7},
    4: {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'quantity': 2},
    5: {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'quantity': 6},
    6: {'title': 'To the Lighthouse', 'author': 'Virginia Woolf', 'quantity': 4},
    7: {'title': 'Brave New World', 'author': 'Aldous Huxley', 'quantity': 8},
    8: {'title': 'Moby-Dick', 'author': 'Herman Melville', 'quantity': 1},
    9: {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'quantity': 9},
    10: {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'quantity': 3}
}


users={}

transactions=[]

def display_catalog():
    print("Catalog:")
    for book_id, book_info in catalog.items():
        availability="Available" if book_info['quantity'] > 0 else "Not Available"
        print(f"{book_id}. {book_info['title']} by {book_info['author']} - {availability}")

def register_user():
    user_id=input("Enter your unique user ID: ")
    user_name=input("Enter your name: ")
    users[user_id]={'name': user_name, 'books_checked_out': {}}

def checkout_book():
    user_id=input("Enter your user ID: ")
    if user_id not in users:
        print("User not registered. Please register first.")
        return

    book_id=int(input("Enter the book ID to check out: "))
    if book_id not in catalog or catalog[book_id]['quantity'] == 0:
        print("Book not available for checkout.")
        return

    if len(users[user_id]['books_checked_out'])>=3:
        print("You have reached the maximum limit of checked-out books (3).")
        return

    checkout_date=datetime.now().strftime("%Y-%m-%d")#concept from net
    due_date=(datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")#concept from net

    transactions.append({'user_id': user_id, 'book_id': book_id, 'checkout_date': checkout_date, 'due_date': due_date})
    users[user_id]['books_checked_out'][book_id] = due_date
    catalog[book_id]['quantity']-=1
    print("Book checked out successfully.")

def return_book():
    user_id=input("Enter your user ID: ")
    if user_id not in users:
        print("User not registered. Please register first.")
        return

    book_id=int(input("Enter the book ID to return: "))
    if book_id not in catalog:
        print("Invalid book ID.")
        return

    if book_id not in users[user_id]['books_checked_out']:
        print("This book is not checked out by you.")
        return

    return_date=datetime.now().strftime("%Y-%m-%d")#concept from net
    due_date = datetime.strptime(users[user_id]['books_checked_out'][book_id], "%Y-%m-%d")#concept from net
    
    days_overdue=max(0,(datetime.now()-due_date).days)#concept from net
    fine=days_overdue*1

    catalog[book_id]['quantity'] += 1
    del users[user_id]['books_checked_out'][book_id]

    print("Book returned successfully.")
    if days_overdue>0:
        print(f"Overdue fine: ${fine}")

def display_overdue_books():
    user_id = input("Enter your user ID: ")
    if user_id not in users:
        print("User not registered. Please register first.")
        return

    overdue_books=[]
    total_fine=0

    for transaction in transactions:
        if transaction['user_id']==user_id:
            due_date=datetime.strptime(transaction['due_date'], "%Y-%m-%d")
            if due_date<datetime.now():
                days_overdue=(datetime.now()-due_date).days#concept from net
                fine=days_overdue * 1
                total_fine+=fine
                overdue_books.append((transaction['book_id'], days_overdue, fine))

    if not overdue_books:
        print("No overdue books.")
    else:
        print("Overdue Books:")
        for book_id, days_overdue, fine in overdue_books:
            print(f"Book ID {book_id}: Overdue by {days_overdue} days. Fine: ${fine}")
        print(f"Total Fine: ${total_fine}")

def display_menu():
    print("\nMenu:")
    print("1. Display Catalog")
    print("2. Register User")
    print("3. Checkout Book")
    print("4. Return Book")
    print("5. Display Overdue Books and Fines")
    print("6. Exit")


while True:
    display_menu()
    choice=input("Enter your choice (1-6): ")

    if choice=='1':
        display_catalog()
    elif choice=='2':
        register_user()
    elif choice=='3':
        checkout_book()
    elif choice=='4':
        return_book()
    elif choice=='5':
        display_overdue_books()
    elif choice=='6':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

