name = input('Enter the name: ')
surname = input('Enter the surname: ')
year = input("Enter the Experience: ")
message = 'Hello %s %s' % (name, surname)
print(message)
message = f"Hello {name} {surname}"
#message = f"Hello {user_input}"
print(message)
print("Hi {} , You have {} years of experience.".format(name, year))