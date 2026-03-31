from connect import get_connection


def call_search():
    pattern = input("Enter search pattern: ")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def call_upsert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def call_bulk():
    names = input("Enter names (comma separated): ").split(',')
    phones = input("Enter phones (comma separated): ").split(',')

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many(%s, %s)", (names, phones))

    conn.commit()
    cur.close()
    conn.close()


def call_pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def call_delete():
    value = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\nPhoneBook (Functions & Procedures)")
        print("1. Search")
        print("2. Upsert")
        print("3. Bulk insert")
        print("4. Pagination")
        print("5. Delete")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == '1':
            call_search()
        elif choice == '2':
            call_upsert()
        elif choice == '3':
            call_bulk()
        elif choice == '4':
            call_pagination()
        elif choice == '5':
            call_delete()
        elif choice == '6':
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()