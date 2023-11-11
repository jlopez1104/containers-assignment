school_subjects = ['Math','Science','Religion','Comp Sci','French','Gym']
print("Current list:", school_subjects)

remove = input("Enter the element to remove: ")

if remove in school_subjects:
    school_subjects.remove(remove)
    print({remove}," was removed from the list")
else:
    print({remove}," is not in the list")

print("Updated list:", school_subjects)