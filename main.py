# our spravochnik
spravochnik = list()

# getting the content that is already in spravochnik file
# and putting it to our "virtual" spravochnik list()

source_file = open("dict.txt", "r")
src = source_file.readlines()
for line in src:
    line = line.split(' ')
    spravochnik.append({"first_name": line[0],
                        "last_name": line[1],
                        "phone": line[2]})
source_file.close()


def printer(source):
    print()
    for person in source:
        print(person['first_name'] + " " + person['last_name'] + " " + person['phone'], end='')
    print('\n')

def show():
    print()
    for person in spravochnik:
        printer(spravochnik)
    print('\n')


# checks whether a person is already in the spravochnik
def full_name_checker(first_name, last_name):
    i = 0
    for person in spravochnik:
        if person.get('first_name') == first_name and person.get('last_name') == last_name:
            return -1, i
        i += 1


def finder():
    command = ''
    print("Find by:")
    print("First name")
    print("Last name")
    print("Full name")
    print("Phone number")
    while True:
        command = input()
        if command == 'First name' or command == 'Last name'or command == 'Full name' or command == 'Phone number':
            print(command + ": ", end='')
            command = command.lower().replace(' ', '_')
            out_people = list()
            val = input()
            for person in spravochnik:
                if person[command] == val:
                    out_people.append(person)
            if len(out_people) == 0:
                print('Sorry. No such person in the spravochnik')
            else:
                printer(out_people)
            break
        print('No such option. Try again.')


# function to add a new person to spravochnik
# also can handle the situations, when a person is
# already in spravochnik
def adder():
    print("Name")
    first_name = input()
    print("Last Name")
    last_name = input()
    check = full_name_checker(first_name, last_name)
    if check[0] == -1:
        print("Hey..wait a minute, such person already in the list!")
        print("You wanna change info or skip?")
        command = 0
        while command != "change" or command != "skip":
            print("Available commands: ")
            print("change/skip")
            command = input()
        if command == "change":
            print("what do you want to change?")
            print("Options: tel/..")
            command = input()
            if command == 'tel':
                print("please enter the new value:")
                new_tel = input()
                spravochnik[check[1]]['phone'] = new_tel
                return
        elif command == 'skip':
            return
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
        print("Available commands: ")
        print("add/show/exit/find")
        print("Waiting for commands...")

        command = input()
        if command == 'add':
            print("adding...")
            adder()
        elif command == 'show':
            print("Let's have a look!")
            show()
        elif command == "find":
            print("Let's have a look..")
            finder()
        elif command != "exit":
            print("What do you mean?")

    file = open('dict.txt', 'w')
    for person in spravochnik:
        file.write(" ".join(person.values()))
    file.close()


main()
