# logic
wanted_book = input()
book_name = ""
book_count = 0

while book_name != wanted_book:
    book_name = input()
    if book_name == wanted_book:
        print(f"You checked {book_count} books and found it.")
        break
    elif book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break
    else:
        book_count += 1
        continue
