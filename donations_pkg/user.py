def login(database, username, password):

    if username not in database and password not in database:
        print("Welcome", username)
        return username

    elif username in database and password not in database:
        print("Incorrect password")
        return ""

def register(database, username):
    if username in database:
        print("Username already exists")
        return ""

    else:
        print(username, "had been registered!")
        return username
