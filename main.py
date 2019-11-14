# our spravochnik
spravochnik = list()

# getting the content that is already in spravochnik file
# and putting it to our "virtual" spravochnik list()

source_file = open("dict.txt", "r")
source = source_file.readlines()
for line in source:
    line = line.split(' ')
    spravochnik.append({"first_name": line[0],
                        "last_name": line[1],
                        "phone": line[2]})
source_file.close()


# checks whether a person is already in the spravochnik
def checker(first_name, last_name):
    i = 0
    for person in spravochnik:
        if person.get('first_name') == first_name and person.get('last_name') == last_name:
            return -1, i
        i += 1


# function to add a new person to spravochnik
# also can handle the situations, when a person is
# already in spravochnik
def adder():
    print("Name")
    first_name = input()
    print("Last Name")
    last_name = input()
    check = checker(first_name, last_name)
    if check[0] == -1:
        print("Hey..wait a minute, such person already in the list! bye!!")
        print("You wanna change info or skip?")
        command = input()
        if command == "change":
            print("what do you want to change?")
            print("Options: tel/..")
            command = input()
            while command != 'return':
                if command == 'tel':
                    print("please enter the new value:")
                    new_tel = input()
                    spravochnik[check[1]]['phone'] = new_tel

    print("Phone")
    raw_phone = input()
    if raw_phone[0] == '+':
        phone = '8' + raw_phone[2:]
    else:
        phone = raw_phone
    spravochnik.append({"first_name": first_name,
                        "last_name": last_name,
                        "phone": phone})


def main():
    command = 0
    while command != 'exit':
        print("Waiting for commands...")
        command = input()
        if command == 'add':
            print("adding...")
            adder()
        elif command == 'show':
            print("lit's have a look!")
        else:
            print("What do you mean?")

    file = open('dict.txt', 'w')
    for person in spravochnik:
        file.write(" ".join(person.values()))
    file.close()


main()
