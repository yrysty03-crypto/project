import os
from connect import get_connection

# ✅ Force UTF-8 for Python I/O
os.environ["PYTHONIOENCODING"] = "utf-8"


# ---------- ADD CONTACT ----------
def add_contact():
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    birthday = input("Birthday (YYYY-MM-DD): ").strip()
    group = input("Group (Family/Work/Friend/Other): ").strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        # Ensure UTF-8 inside PostgreSQL session
        cur.execute("SET client_encoding TO 'UTF8'")

        # insert group if not exists
        cur.execute("""
            INSERT INTO groups(name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
        """, (group,))

        # get group id
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        group_id = cur.fetchone()[0]

        # insert contact
        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (name, email, birthday, group_id))

        contact_id = cur.fetchone()[0]

        conn.commit()
        print("✅ Contact added!")

        add_phone(contact_id)

    except Exception as e:
        print("❌ Error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


# ---------- ADD PHONE ----------
def add_phone(contact_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SET client_encoding TO 'UTF8'")

        while True:
            phone = input("Phone: ").strip()
            ptype = input("Type (home/work/mobile): ").strip().lower()

            if ptype not in ['home', 'work', 'mobile']:
                print("❌ Invalid type")
                continue

            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, phone, ptype))

            more = input("Add another phone? (y/n): ").strip().lower()
            if more != 'y':
                break

        conn.commit()

    except Exception as e:
        print("❌ Error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


# ---------- VIEW CONTACTS ----------
def view_contacts():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SET client_encoding TO 'UTF8'")

        cur.execute("""
            SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            ORDER BY c.name
        """)

        rows = cur.fetchall()

        if not rows:
            print("No contacts found.")
        else:
            for row in rows:
                print(row)

    except Exception as e:
        print("❌ Error:", e)

    finally:
        cur.close()
        conn.close()


# ---------- DELETE CONTACT ----------
def delete_contact():
    name = input("Enter name to delete: ").strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SET client_encoding TO 'UTF8'")

        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
        conn.commit()

        if cur.rowcount == 0:
            print("No contact found.")
        else:
            print("✅ Contact deleted.")

    except Exception as e:
        print("❌ Error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


# ---------- MENU ----------
def menu():
    while True:
        print("\n📱 Extended PhoneBook")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    menu()