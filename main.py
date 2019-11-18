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
                        "phone_number": line[2]})
source_file.close()


def printer(source):
    print()
    for person in source:
        print(person['first_name'] + " " + person['last_name'] + " " + person['phone_number'], end='')
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
    print("..or exit..")
    out_people = list()
    while True:
        command = input()
        if command == 'exit':
            break
        if command == 'First name':
            print('First name: ', end='')
            val = input()
            for person in spravochnik:
                if person['first_name'] == val:
                    out_people.append(person)
            if len(out_people) != 0:
                print('Here are the variants:')
                printer(out_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Last name':
            print('Last name: ', end='')
            val = input()
            for person in spravochnik:
                if person['last_name'] == val:
                    out_people.append(person)
            if len(out_people) != 0:
                print('Here are the variants:')
                printer(out_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Full name':
            print('Full name: ', end='')
            val = input().split()
            for person in spravochnik:
                if person['first_name'] == val[0] and person['last_name'] == val[1]:
                    out_people.append(person)
            if len(out_people) != 0:
                print('Here are the variants:')
                printer(out_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Phone number':
            print('Phone number: ', end='')
            val = input()
            for person in spravochnik:
                if person['phone_number'] == val:
                    out_people.append(person)
            if len(out_people) != 0:
                print('Here are the variants:')
                printer(out_people)
            else:
                print('Sorry, no matches')
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
                spravochnik[check[1]]['phone_number'] = new_tel
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
                        "phone_number": phone})


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
            print("Have a look!")
            printer(spravochnik)
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
