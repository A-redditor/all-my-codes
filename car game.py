start = False
print ('type help for the list of commands!')
while True:
    command = input('> ').lower() #instead of using command.lower() over and over
    while command != 'help' and command != 'quit' and command != 'stop' and command != 'start':
        print ("that's not a command...")
        command = input ('> ').lower()
    match command:
        case 'help':
            print ('''start: to start the car
stop: to stop the car
quit: to terminate the  program''')
        case 'start':
            if not start:
                print ('the car has started')
                start = True
            else:
                print ('the car is already started')
        case 'stop':
            if start:
                print ('the car has stopped')
                start = False
            else:
                print ('the car is already stopped')
        case 'quit':
            break
