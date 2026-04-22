import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL
)
""")
conn.commit()


def add_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        (name, age, email)
    )
    conn.commit()
    print("Record added successfully!\n")


def view_records():
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    if not records:
        print("Database is empty.\n")
        return

    print("\n--- Database Records ---")
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}")
    print()


def main():
    while True:
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

    conn.close()


if __name__ == "__main__":
    main()
