import os.path
import json

User = {}
filename = "userDB.json"

def add_user():
    output = {}
    print("please describe your details")
    a = input("Enter your name:")
    b = input("Enter your age:")
    c = input("Enter your address:")
    d = input("Gender:")
    output["Name"] = a
    output["Age"] = b
    output["Address"] = c
    output["Gender"] = d
    return output


def get_user_by_id(user_id):
    curr_user = {}
    if user_id in User:
        curr_user = User[user_id]
    return curr_user


def remove_user_by_id(user_id):
    if user_id in User:
        del User[user_id]
        print("User deleted")
    else:
        print("User not found")
    return


def modify_user(user_id):
    if user_id in User:
        User[user_id] = add_user()
        print(f"user {user_id} updated.")
    else:
        print("User not found")


def menu():
    print("\n\nMenu")
    print("1.Add user")
    print("2.Display user by id")
    print("3.Display all users")
    print("4.Remove user")
    print("5.Modify user")
    print("6.Exit\n")
    return int(input("Enter choice:"))

def getExistingRecords():
    data = {}
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
                data = json.loads(f.read())
        f.close()
    else:
        print(f"No existing data present. File not found {filename}")
    return data


def storeExistingData(data):
    with open(filename, "w+") as f:
        json.dump(data, f, indent=4)
    f.close()
    print("Saved info to file successfully.")


if __name__ == "__main__":
    User = getExistingRecords()
    User_count = len(User) +1
    choice = True
    while choice:
        c = menu()
        if c == 1:
            g = add_user()
            print(g)
            User[User_count] = g
            User_count += 1

        if c == 2:
            h = int(input("Enter user id:"))
            u = get_user_by_id(str(h))

            if u == {}:
                print(f"User with this id {h} not found.")
            else:
                print(u)

        if c == 3:
            if User == {}:
                print("No users are present")
            else:
                print(User)

        if c == 4:
            v = int(input("Enter the id to remove the user:"))
            remove_user_by_id(v)

        if c == 5:
            m = int(input("Enter the user id which you want to modify:"))
            modify_user(m)

        if c == 6:
            storeExistingData(User)
            choice = False
            print("Program exited succsessfully.")
