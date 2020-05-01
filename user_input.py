def temps(value):
    if len(value) >= 5 and len(value) < 10 :
        print('Between 5 and 10')
        return value
    elif len(value) >= 10 and len(value) < 20 :
        print('Between 10 and 20')
        return value
    else:
        print('Above 20')
        return value

output_Value = temps(input('Enter the value : '))
print(output_Value.upper());
    