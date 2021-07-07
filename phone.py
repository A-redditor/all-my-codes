contacts = {}
ContactsByName = {}
print ('type help  for the list of commands :D')

def SaveContact(contacts, ContactsByName):
    number  = input('please type their phone number: ')
    while number in contacts:
        exists = contacts[number]
        print(f'this contact already exists under the name "{exists}"')
        number = input ('type a new phone number: ')
    name = input(f'what should be the name for {number} ')
    while name in ContactsByName:
        print (f'this contact already exists with the number {ContactsByName[name]}')
        name = input ('please enter a new name: ')
    print ('contact saved successfully')
    return number, name
while True:
    command = input ('> ').lower().strip()
    while command != 'exit' and command != 'save a new contact' and command != 'find' and command != 'edit' and command != 'help':
        print('this is not a command...')
        command = input('> ').lower().strip
    match command:
        case 'exit':
            break
        case 'save a new contact':
            PhoneNumber, name = SaveContact(contacts, ContactsByName)
            contacts [PhoneNumber] = name
            ContactsByName [name] = PhoneNumber
        case'find':
            SearchBy = input('do you want to search by number or name? \n').lower().strip()
            while SearchBy != 'name' and SearchBy != 'number':
                SearchBy = input('do you want to search by number or name? for name type "name" and for number type "number"\n').lower().strip()
            match SearchBy:
                case 'name':
                    find = input('whats their name?\n')
                    found = ContactsByName.get(find, '`null`')
                    print(f'their phone number is {found}')
                case 'number':
                    find = input('whats their phone number?\n')
                    found = contacts.get(find, '`null`')
                    print (f'their name is {found}')
        case 'edit':
            number = input('whats their phone number? \n')
            while number not in contacts:
                print ('this number does not exist')
                number = input('write a corrct number ')
            ToEdit = contacts[number]
            new_name = input('enter a new name: ')
            while new_name in ContactsByName:
                print ('this name already exists')
                new_name = input ('please enter a new name: ')
            contacts [number] = new_name
            ContactsByName.pop(ToEdit)
            ContactsByName [new_name] = number
            print ('contact edited successfully')
        case 'help':
            print ('''the commands are:
save a new contact: to save a new contact
edit: to edit an existing contact
find: to find a saved contact
exit: to quit the app''')
