library = []

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "title": title,
        "author": author,
        "issued": False
    }

    library.append(book)
    print("\nBook Added Successfully!\n")


def view_books():
    if len(library) == 0:
        print("\nNo Books Available!\n")
        return

    print("\nLibrary Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"

        print(
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {status}"
        )

    print()


def search_book():
    title = input("Enter Book Title: ")

    for book in library:
        if book["title"].lower() == title.lower():
            print("\nBook Found:")
            print(book)
            return

    print("\nBook Not Found!\n")


def issue_book():
    title = input("Enter Book Title to Issue: ")

    for book in library:
        if book["title"].lower() == title.lower():

            if book["issued"]:
                print("\nBook Already Issued!\n")

            else:
                book["issued"] = True
                print("\nBook Issued Successfully!\n")

            return

    print("\nBook Not Found!\n")


def return_book():
    title = input("Enter Book Title to Return: ")

    for book in library:
        if book["title"].lower() == title.lower():

            if not book["issued"]:
                print("\nBook Was Not Issued!\n")

            else:
                book["issued"] = False
                print("\nBook Returned Successfully!\n")

            return

    print("\nBook Not Found!\n")


def delete_book():
    title = input("Enter Book Title to Delete: ")

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)

            print("\nBook Deleted Successfully!\n")
            return

    print("\nBook Not Found!\n")


while True:

    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")