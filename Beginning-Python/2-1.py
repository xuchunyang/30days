months = ['Jan', 'Feb', 'Mar', "Apr", 'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec']

endings = ['st', 'nd', 'rd'] + \
    17 * ['th'] + ['st', 'nd', 'rd'] + \
    7 * ['th'] + ['st']


year = input('Year: ')
month = input('Month: ')
day = input('Day: ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(year, month_name, ordinal)
