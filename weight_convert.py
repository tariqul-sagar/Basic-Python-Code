set = int(input('Which conversion do you want:(Just reply 1 or  2)\n1. Pounds to Kilograms\n2. Kilograms to Pounds\n'))

if(set == 1):
    weight = float(input('Enter your Weight (in pound): '))
    convert = weight / 2.2046
    print('You weight is ',convert,'kilograms')
elif(set == 2):
    weight = float(input('Enter your Weight (in Kilograms): '))
    convert = weight * 2.2046
    print('You weight is ',convert,'Pounds(lbs)')
else:
    print('Please type only 1 or 2')
