from prettytable import PrettyTable
import datetime
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
    return 0, 0


def remover():
    while True:
        print('Enter first name:', end=' ')
        first_name = input()
        print('Enter last name:', end=' ')
        last_name = input()
        check = full_name_checker(first_name, last_name)
        if check[0] == -1:
            spravochnik.pop(check[1])
            sort_spravochnik()
            return
        else:
            print('No such person.')
            print('1. Try again')
            print('2. Exit')
            command = input()
            if command == '2':
                return


def sort_spravochnik():
    spravochnik.sort(key=lambda p: p['last_name'])


def changer(found_people):
    print('Do you want to change anything?')
    print('Yes/No')
    val = input()
    if val == 'Yes':
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
                    found_person = found_people[val-1]
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
                val = phone_adder()
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['phone_number'] = val
                print('Done')
            if command == 'Birth date':
                val = birth_adder()
                i = full_name_checker(found_person['first_name'], found_person['last_name'])
                spravochnik[i[1]]['birth_date'] = val
                print('Done')
    if val == 'No':
        return
    sort_spravochnik()


# function allows to find a certain person using options
def finder():
    print("Find by:")
    print("1. First name")
    print("2. Last name")
    print("3. Full name")
    print("4. Phone number")
    print("5. Exit\n")
    found_people = list()
    while True:
        command = input('Choose the number: ')
        if command == '5':
            return
        if command == '1':
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
                print('Sorry, no matches\n')
            break

        if command == '2':
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
                print('Sorry, no matches\n')
            break
        if command == '3':
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
                print('Sorry, no matches\n')
            break
        if command == '4':
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
                print('Sorry, no matches\n')
            break
        print('No such option. Try again.')


def phone_adder():
    while True:
        print("Phone number:", end=' ')
        val = input()
        if val[0] == '+':
            val = '8' + val[2:]
        if len(val) == 11:
            return val
        elif len(val) > 11:
            print('Line too long. Try again.')
        elif len(val) < 11:
            print('Line to short. Try again.')


def birth_adder():
    while True:
        print('Birth date(dd.mm.yyyy):', end=' ')
        val = input()
        if len(val) == 10:
            d = val.split('.')
            try:
                date = datetime.date(int(d[2]), int(d[1]), int(d[0]))
                return date.strftime('%x')
            except ValueError:
                print("Wrong data. Try again")
        else:
            print("Try again")


# function allows to add a new person to spravochnik
# handles the situations, when a person is already in spravochnik
def adder():
    print("First name: ")
    first_name = input()
    print("Last Name: ")
    last_name = input()
    check = full_name_checker(first_name, last_name)
    if check[0] == -1:
        print("Hey..wait a minute, such person is already in the list!")
        while True:
            print("Do you want to change info or exit?")
            command = input()
            if command == 'exit':
                return
            if command == 'change':
                person = list()
                person.append(spravochnik[check[1]])
                changer(person)
                return

    phone = phone_adder()
    print('Birth date: ')
    bd = birth_adder()
    spravochnik.append({"first_name": first_name,
                        "last_name": last_name,
                        "phone_number": phone,
                        "birth_date": bd})
    sort_spravochnik()


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

    print("\n-------Welcome to directory!-------")
    while True:
        print("\nChoose what you want to do: ")
        print('1. Add a new person')
        print('2. Show the contents')
        print('3. Find a person')
        print('4. Remove a record')
        print('5. I wanna go to mummy\n')
        command = input('Here: ')
        if command == '5':
            print('Bye!\n')
            break
        elif command == '1':
            print("\n------- Adding a new person --------\n")
            adder()
        elif command == '2':
            printer(spravochnik)
        elif command == "3":
            finder()
        elif command == '4':
            remover()
        else:
            print("What do you mean?")

    file = open('dict.txt', 'w')
    for person in spravochnik:
        file.write(" ".join(person.values()) + "\n")
    file.close()


if __name__ == '__main__':
    main()
