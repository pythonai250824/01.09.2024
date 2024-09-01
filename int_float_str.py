
# int = integer number .. -100, 0, 4324
# str = string .. 'Enter number:' "Enter number:" 'What's your name?"
# x: int = input('Enter number:')

x: int = 555
my_name: str = 'Itay'
ph_number: str =  '03-55555555'
code_atm: int = 1234
code_atm_str: str = '1234' #  '1','2','3','4'
height: float = 1.93
height1: float = 1.85
height2: float = 1.99

print(my_name)

print(5, type(5))
print(99.1, type(99.1))
print(0.0, type(0.0))
print("x", type(x))  # 555
y: str = '55'
print("y", type(y))  # '55'


z: int = input('test the input:')  # get from keyboard
z = int(z)
print(z + 2)

t = int(input('test the input:'))  # correct
print(t + 2)
# 5
# your-name
# what is the type of z

my_height: float = float(input('enter your height:'))

# input weight from the user and use float to change it to float
# print weight - 10
my_weight: float = float(input('enter your weight:'))
print(my_weight - 10)

# input year of birth from the user and use int to change it to int
# print year of birth + 10
year_of_birth: int = int(input('enter your year of birth:'))  # casting
print(year_of_birth + 10)






