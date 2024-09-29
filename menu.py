def display_menu():
    print("1. Initialize Database with Quotes")
    print("2. Get a Random Quote")
    print("3. Add a New Quote")
    print("4. Exit")

if __name__ == "__main__":
    import init_db
    import get_quote
    import add_quote

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            init_db.initialize_db()
        elif choice == "2":
            get_quote.get_random_quote()
        elif choice == "3":
            new_quote = input("Enter the quote: ")
            author_name = input("Enter the author's name: ")
            add_quote.add_quote(new_quote, author_name)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

