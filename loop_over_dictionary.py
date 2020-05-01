name_and_age = {"Chandan":28,"Neha":29,"Heelo":30}

for val in name_and_age.items():
    print(val)

for val in name_and_age.keys():
    print(val)

for val in name_and_age.values():
    print(val)


for val in name_and_age.items():
    print("Name {} and Age {} ".format(val[0], val[1]))

for key, value in name_and_age.items():
    print("Name {} and Age {} ".format(key, value))