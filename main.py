from prettytable import PrettyTable
# our spravochnik
spravochnik = list()


# function to print the whole spravochnik
def printer(source):
    if len(source) == 0:
        print('It is empty!')
        return
    print()
    t = PrettyTable()
    t.field_names = [' ', 'First name', 'Last name', 'Phone number', 'Birth date']
    i = 1
    for person in source:
        t.add_row([str(i) + '.', person['first_name'], person['last_name'], person['phone_number'], person['birth_date']])
        i = i + 1
    print(t)


# checks whether a person is already in the spravochnik
# returns the index of a person, if in spravochnik
def full_name_checker(first_name, last_name):
    i = 0
    if len(spravochnik) == 0:
        return 0, 0
    for person in spravochnik:
        if person.get('first_name') == first_name and person.get('last_name') == last_name:
            return -1, i
        i += 1


def changer(found_people):
    print('Do you want to change anything?')
    print('YES/NO')
    val = input()
    if val == 'YES':
        found_person = {}
        if len(found_people) > 1:
            while True:
                print('Whose information do you want to change (print the number): ')
                for x in range(len(found_people)):
                    print(x + 1, end=' ')
                print('or exit')
                val = int(input())
                if val == 'exit':
                    break
                elif 1 <= val <= len(found_people):
                    found_person = found_people[val]
                    break
                elif val > len(found_people):
                    print('Try another number')
        else:
            found_person = found_people[0]
        while True:
            print('What to change?')
            print('Options:')
            print('First name')
            print('Last name')
            print('Phone number')
            print('Birth date')
            print('exit')
            command = input()
            if command == 'exit':
                break
            if command == 'First name':
                print('Print new name: ', end=' ')
                val = input()
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['first_name'] = val
                print('Done!')
            if command == 'Last name':
                print('Print new last name: ', end=' ')
                val = input()
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['last_name'] = val
                print('Done')
            if command == 'Phone number':
                print('Print new phone number: ', end=' ')
                val = input()
                if val[0] == '+':
                    val = '8' + val[2:]
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['phone_number'] = val
                print('Done')
            if command == 'Birth date':
                print('Print new birth date: ', end=' ')
                val = input()
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['birth_date'] = val
                print('Done')

    spravochnik.sort(key=lambda p: p['last_name'])


# function allows to find a certain person using options
def finder():
    print("Find by:")
    print("First name")
    print("Last name")
    print("Full name")
    print("Phone number")
    print('Birth date')
    print("..or exit..")
    found_people = list()
    while True:
        command = input()
        if command == 'exit':
            break
        if command == 'First name':
            print('First name: ', end='')
            val = input()
            for person in spravochnik:
                if person['first_name'] == val:
                    found_people.append(person)
            if len(found_people) != 0:
                print('Here are the variants:')
                printer(found_people)
                changer(found_people)
            else:
                print('Sorry, no matches, try again?')
            break

        if command == 'Last name':
            print('Last name: ', end='')
            val = input()
            for person in spravochnik:
                if person['last_name'] == val:
                    found_people.append(person)
            if len(found_people) != 0:
                print('Here are the variants:')
                printer(found_people)
                changer(found_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Full name':
            print('Full name: ', end='')
            val = input().split()
            for person in spravochnik:
                if person['first_name'] == val[0] and person['last_name'] == val[1]:
                    found_people.append(person)
            if len(found_people) != 0:
                print('Here are the variants:')
                printer(found_people)
                changer(found_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Phone number':
            print('Phone number: ', end='')
            val = input()
            for person in spravochnik:
                if person['phone_number'] == val:
                    found_people.append(person)
            if len(found_people) != 0:
                print('Here are the variants:')
                printer(found_people)
                changer(found_people)
            else:
                print('Sorry, no matches')
            break
        if command == 'Birth date':
            print('Birth date: ', end='')
            val = input()
            for person in spravochnik:
                if person['birth_date'] == val:
                    found_people.append(person)
            if len(found_people) != 0:
                print('Here are the variants:')
                printer(found_people)
                changer(found_people)
            else:
                print('Sorry, no matches')
            break

        print('No such option. Try again.')


# function allows to add a new person to spravochnik
# handles the situations, when a person is already in spravochnik
def adder():
    print("Name: ")
    first_name = input()
    print("Last Name: ")
    last_name = input()
    check = full_name_checker(first_name, last_name)
    if check[0] == -1:
        print("Hey..wait a minute, such person is already in the list!")
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
    print("Phone: ")
    raw_phone = input()
    if raw_phone[0] == '+':
        phone = '8' + raw_phone[2:]
    else:
        phone = raw_phone

    print('Birth date: ')
    bd = input()
    spravochnik.append({"first_name": first_name,
                        "last_name": last_name,
                        "phone_number": phone,
                        "birth_date": bd})


def main():
    # getting the content that is already in spravochnik file
    # and putting it to our "virtual" spravochnik list()
    source_file = open("dict.txt", "r")
    src = source_file.readlines()
    for line in src:
        line = line.split(' ')
        spravochnik.append({"first_name": line[0],
                            "last_name": line[1],
                            "phone_number": line[2],
                            'birth_date': line[3].replace('\n', '')})
    source_file.close()
    spravochnik.sort(key=lambda p: p['last_name'])

    print("Welcome!\n")
    while True:
        print("Available commands: ")
        print("add/show/exit/find\n")

        command = input()
        if command == 'exit':
            break
        elif command == 'add':
            print("adding...")
            adder()
        elif command == 'show':
            # print("Have a look!")
            printer(spravochnik)
        elif command == "find":
            print("Let's have a look..")
            finder()
        else:
            print("What do you mean?")

    file = open('dict.txt', 'w')
    for person in spravochnik:
        file.write(" ".join(person.values()) + "\n")
    file.close()


if __name__ == '__main__':
    main()
