colours = ['blue','red','yellow','gray','black','white','green','purple','pink','orange']
print('these are colours in list',colours)
while True:
    colour1 = int(input('please enter a number from 0 to 4: '))
    if input == '0'or'1'or'2'or'3'or'4':
        while True:
            colour2 = int(input('please enter a numeber from 5 to 9: '))
            if input == '5'or'6'or'7'or'8'or'9':
                print('your 2 colours are',colours[colour1],'and',colours[colour2])
                break
            else:
                print('please enter valid number')
    else:
        print ('please enter correct number')
