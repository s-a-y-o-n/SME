
from getpass import getpass

from app.database.connection import SessionLocal
from app.models.user import User
from app.core.security import hash_password


def create_staff_user():

    db = SessionLocal()

    try:
        name = input("Enter full name: ")
        email = input("Enter email: ").strip().lower()

        print("\nSelect role:")
        print("1. Relationship Manager")
        print("2. Loan Officer")

        choice = input("Enter choice: ")

        roles = {
            "1": "relationship_manager",
            "2": "loan_officer"
        }

        role = roles.get(choice)

        if not role:
            print("Invalid role")
            return

        password = getpass("Enter password: ")

        if len(password) < 8:
            print("Password must contain at least 8 characters")
            return

        if db.query(User).filter(User.email == email).first():
            print("Email already exists")
            return

        user = User(
            full_name=name,
            email=email,
            hashed_password=hash_password(password),
            role=role
        )

        db.add(user)
        db.commit()

        print(f"\n{role} account created successfully!")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    create_staff_user()
