#this is a python comment

print(complex(2+4j) +5)
print("The old pond\nA frog jumped in,\nKerplunk!")
print("Kenneth Arthur\nThe guy from Prempeh College, \nis now at KNUST")

num = 15
if num > 12:
    print('number is more than 12')
elif num <= 12:
    print('number is less than 12')
elif num < 12:
    print('number is not 12')
else:
    print('number is 12')
    
quantity = 14
unit_price = 26.99
extended_price = quantity * unit_price
print(extended_price)    

message = """ 
Hi, 
i'm at home right now 
so u can come over.
Ken.. thank u 
 """
print(message)

name = 'kenneth'
print(name[0:3])

first = 'snr'
last = 'ken'
full_name =f'{first} [{last}] is an Amanfour'
print(full_name)
print('snr' in last)
print(len(first))
print(len(message))

print(message.lower())
print(message.find('Hi'))

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')

#comparison operators
temperature = 35
while temperature <= 40:
    print(temperature)
    temperature += 1
print("It's not a hot day")

name = 'Kenneth'
if len(name) < 3:
    print('name must be atleast three')
elif len(name) > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good')
    
i = 1
while i <= 5:
    print(i)
    
    i = i+1
print('done')

name = 1
while name >= 8:
    print(name)
    name += 1
print('done')

for E in range(1000, 1010):
    for N in range(2000, 2010):
        print(f"({E}, {N})")

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('*' * number)
print('well done')

A= [
  [31.4977, -34.6996],
  [19.3257, 71.1214],
  [-50.8234, -36.4218],
  [0.7404, 0.6721],
  [-0.5825, 0.8128]
 ]

W= [
    [0.04, 0, 0, 0, 0],
    [0, 0.04, 0, 0, 0],
    [0, 0, 0.04, 0, 0],
    [0, 0, 0, 1600, 0],
    [0, 0, 0, 0, 1600]
  ]

L= [
    [0],
    [-13],
    [14],
    [0],
    [-0.189]
   ]


V= [
    [8.376334528],
    [4.146409799],
    [-13.52274433],
    [-0.028379207],
    [0.0081871585]
   ]

X= [
    [0.0991222695],
    [-0.1514199305]
   ]


def greet_user():
    print('Hi there!')
    print('Welcome on board')
    
print('start')
greet_user()
print('finish')


price = 1000000
good_credit = True

if good_credit:
    down_payment= 0.1 * price
else:
    down_payment= 0.2 * price
print(f'Down Payment: ${down_payment:,.2f}')
print('enjoy your stay')

temperature = 35
if temperature > 30:
    print("it's a hot day")
elif temperature == 35:
    print("it's a normal day")
elif temperature < 30:
    print("it's a cold a day")
else:
    print("it's a lovely day")
    
name = "Kenneth"
if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name must be a maximum of 50 characters')
else:
    print('name looks good')

weight = float(input('weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = 0.45 * weight
    print(f'you are {converted} kilos')
else:
    converted = weight/0.45
    print(f'you are {converted} pounds')
print('Done')


# Try and Exceptions (sidestepping error) 

try:
    numba = int(input('Enter a number: '))
    print(numba)

except ValueError:
    print('invalid input')
    

