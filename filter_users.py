import json


def filter_users_by_name(name):
    """Filters and prints users by name."""
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        print("File: users.json not found")
        return

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if not filtered_users:
        print(f"No users found with the name '{name}'.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_age(age):
    """Filters and prints users by age."""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File: users.json not found")
        return

    filtered_users = [user for user in users if user["age"] == age]

    if not filtered_users:
        print(f"No users found with the age '{age}'.")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_email(email):
    """Filters and prints users by email."""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File: users.json not found")
        return

    filtered_users = [user for user in users if user["email"] == email]

    if not filtered_users:
        print(f"No users found with the age '{email}'.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = (
        input("What would you like to filter by (" "name, age, email):").strip().lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email-address to filter users: ")
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
