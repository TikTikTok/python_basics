def getPhrase(value):
    titlize = value.capitalize()
    print(titlize)
    queuess = ("How","Why","What")
    if  value.startswith(queuess):
        result = '{} ?'.format(titlize)
    else :
        result = '{}.'.format(titlize)
    return result

paragraph = []
result = " "
while True:
    user_input = input('Enter Something: ')
    if user_input == "\\end":
        break
    else:
        paragraph.append(getPhrase(user_input))

print(result.join(paragraph))

for strs in paragraph:
    print(strs)

    


    

