import csv
from connect import get_connection


# ---------- TABLE SETUP ----------
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


# ---------- INSERT FROM CSV (FINAL FIX) ----------
def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()

    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        next(reader, None)  # ✅ skip header row

        for row in reader:
            if not row or len(row) < 2:
                print(f"Skipping invalid row: {row}")
                continue

            name, phone = row[0].strip(), row[1].strip()

            if not name or not phone:
                print(f"Skipping empty values: {row}")
                continue

            try:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                    (name, phone)
                )
            except Exception as e:
                print(f"Error inserting {row}: {e}")

    conn.commit()
    cur.close()
    conn.close()


# ---------- INSERT FROM CONSOLE ----------
def insert_from_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# ---------- UPDATE ----------
def update_contact(old_name):
    conn = get_connection()
    cur = conn.cursor()

    new_name = input("New name (leave empty to skip): ").strip()
    new_phone = input("New phone (leave empty to skip): ").strip()

    if new_name:
        cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, old_name))

    conn.commit()
    cur.close()
    conn.close()


# ---------- QUERY ----------
def query_contacts():
    conn = get_connection()
    cur = conn.cursor()

    print("1. Search by name")
    print("2. Search by phone prefix")
    choice = input("Choose option: ")

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == '2':
        prefix = input("Enter prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        print("Invalid choice")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ---------- DELETE ----------
def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    value = input("Enter name or phone: ")
    cur.execute("DELETE FROM contacts WHERE name=%s OR phone=%s", (value, value))

    conn.commit()
    cur.close()
    conn.close()


# ---------- MENU ----------
def menu():
    create_table()

    while True:
        print("\nPhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == '1':
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            name = input("Enter existing name: ")
            update_contact(name)
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()