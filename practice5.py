favorite_foods = {}
for i in range(1, 5):
    food = input(f"Enter your favorite food : ")
    favorite_foods[i] = food
print(favorite_foods)
choice = input("would you like to remove food?(y/n): ")
while True:
    if choice == 'y':
        item_name = input('please enter an item in list you wish to remove: ')
        if item_name in favorite_foods:
            del favorite_foods[item_name]
            print('item successfully removed')
            print("list after removal:")
            print(favorite_foods)
        else:
            print('item you have selected is not currently in list')
    elif choice == 'n':
        print(favorite_foods)
        break
    else:
        print('please select correct answer')
        break
