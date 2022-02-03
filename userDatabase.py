User = {}
def add_user(user_id):
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
    print(f"user id is {user_id}")
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




if __name__ =="__main__":
    User_count = 1
    choice = True
    while choice:
        print("Menu")
        print("1.Add user")
        print("2.Display user by id")
        print("3.Display all users")
        print("4.Remove user")
        print("5.Modify user")
        print("6.Exit")

        c = int(input("Enter choice:"))
        if c == 1:
            g = add_user(User_count)
            print(g)
            User[User_count] = g
            User_count += 1

        if c == 2:
            h  = int(input("Enter user id:"))
            u = get_user_by_id(h)

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

        if c == 6:
           choice = False
           print("Program exited succsessfully.")










