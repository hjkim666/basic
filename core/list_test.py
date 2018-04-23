# IT01_membership.py
# check a user name and PIN code

database = [
    ['albert','1234'],
    ['dilbert','1234'],
    ['smith','1234'],
    ['jones','1234']
]

username = input('User name: ')
pin = input('PIN code: ')

if [username, pin] in database: print('Access granted')

# if [username, pin] in database:
#   print('Access granted')
# else:
#   print('fail')
