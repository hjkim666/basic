# IT01_index.py
# print out a data, given year, month, and day as numbers

months = [
    'January',
    'Faburary',
    'March',
    'April',
    'May',
    'June',
    'Jully',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]


# A list with one ending for each number from 1 to 31
endings = ['st','nd','rd'] + 17 * ['th'] \
          + ['st','nd','rd'] + 7 * ['th'] +['st']

year =input('Year: ')
month =input('Month(1-12): ')
day = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' ' + ordinal + ', ' + year) 


