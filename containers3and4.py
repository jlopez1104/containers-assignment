
name = input("Enter the person's name: ")
height = int(input("Enter the person's height in centimeters: "))
favorite_color = input("Enter the person's favorite color: ")
favorite_musician = input("Enter the person's favourite musician: ")
person_info = {
    'name': name,
    'height': height,
    'favorite_color': favorite_color,
    'favorite_musician': favorite_musician}

print(person_info['name'],"'s height is ",person_info['height']," cm, and their favorite color is ",person_info['favorite_color'],". Also, the their favourite musiscian is: ",person_info['favorite_musician'])
