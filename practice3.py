sports = ['basketball','football']
while True:
    print('Menu')
    print('1. to add sport to list')
    print('2. see list')
    print('3. exit')
    choice = input('please enter 1/2/3: ')
    if choice == '1':
        while True:
            new_sport = input('please enter you favourite sport: ')
            if new_sport in sports:
                print ('sport is already inside list')
                break
            else:
                sports.append(new_sport)
                print('sport successfully added')
                break
    elif choice == '2':
        print('sports:',sports)
    elif choice == '3':
        break
    else:
        print('please select corrrect option')