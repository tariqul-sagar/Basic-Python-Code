import datetime

y = datetime.datetime.now().month
z = datetime.datetime.now().year

birth_month = int(input('\nBirth Month (In number): '))
birth_year = int(input('\nBirth Year: '))

if(birth_month<y):
    if(birth_year<z):
        month = y - birth_month
        year = z - birth_year

        if(month == 12):
            month = 0
            year = year + 1

        print("Your age is " , year ," year " , month , " month ")

else:
    month = 12 - (birth_month - y)
    year = (z - birth_year) - 1

    if (month == 12):
        month = 0
        year = year + 1

    print("Your age is " , year," year " , month, " month ")