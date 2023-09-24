import os
import datetime

# Function to create a new diary entry
def create_entry():
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = input("Write your diary entry:\n")
    with open("diary.txt", "a") as file:
        file.write(f"\nDate: {date}\n")
        file.write(f"{entry}\n")
    print("Entry added successfully!")

# Function to view all diary entries
def view_entries():
    if not os.path.exists("diary.txt"):
        print("No entries found.")
        return
    with open("diary.txt", "r") as file:
        entries = file.read()
        print(entries)

# Function to search for entries containing a specific keyword
def search_entries(keyword):
    if not os.path.exists("diary.txt"):
        print("No entries found.")
        return
    with open("diary.txt", "r") as file:
        entries = file.read()
        if keyword in entries:
            print("Entries containing the keyword:")
            print(entries)

# Main program loop
while True:
    print("\nPersonal Diary")
    print("1. Create a new entry")
    print("2. View all entries")
    print("3. Search for entries")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        keyword = input("Enter a keyword to search for: ")
        search_entries(keyword)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
