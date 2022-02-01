def accept_array(size):
    output = []
    for i in range(size):
        b = int(input(f"Enter the {i + 1} no.:"))
        output.append(b)
    return output

def parse_string_to_array(string):
    output = []
    arr_obj = string.split(",")
    for i in range(len(arr_obj)):
        output.append(int(arr_obj[i]))
    return output

def accept_dict():
    output = {}
    size = int(input("Enter the size of dict:"))
    for i in range(size):
        k = input("Enter the key:")
        v = input("Enter the value:")
        output[k] = v
    return output

def parse_to_dict():
    output = {}
    # 1:abc 2:bcd 3:ghk 4:gsk
    dict_str = input("Enter the dict_string:")
    dict_obj = dict_str.split(" ")
    for i in range(len(dict_obj)):
        curr_element = dict_obj[i]
        if ":" in curr_element:
            curr_obj = curr_element.split(":")
            output[curr_obj[0]] = curr_obj[1]
    return output



if __name__ == "__main__":

    choice = True
    while choice:
        print("**** Menu ****")
        print("1. Accept List")
        print("2. Parse to List")
        print("3. Accept Dict")
        print("4. Parse to dict")
        print("5. Exit")

        c = int(input("Enter choice:"))
        if c == 1:
            a = int(input("Enter size of array:"))
            result = accept_array(a)
            print(result)

        if c == 2:
            a = input("Enter the array in csv form:")
            v = parse_string_to_array(a)
            print(v)

        if c == 3:
            a = accept_dict()
            print(a)

        if c == 4:
            result = parse_to_dict()
            print(result)

        if c == 5:
            choice = False
            print("Program exited successfully")


